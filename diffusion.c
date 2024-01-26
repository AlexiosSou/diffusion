#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "api.h"

#define NX 8192
#define NY 8192

float data[2][NY][NX];

/* in microseconds (us) */
double get_elapsed_time(struct timeval *begin, struct timeval *end)
{
    return (end->tv_sec - begin->tv_sec) * 1000000
        + (end->tv_usec - begin->tv_usec);
}

void init()
{
    int x, y;
    int cx = NX/2, cy = 0; /* center of ink */
    int rad = (NX+NY)/8; /* radius of ink */
    
    for(y = 0; y < NY; y++) {
        for(x = 0; x < NX; x++) {
            float v = 0.0;
            if (((x-cx)*(x-cx)+(y-cy)*(y-cy)) < rad*rad) {
                v = 1.0;
            }
            data[0][y][x] = v;
            data[1][y][x] = v;
        }
    }
    return;
}

/* Calculate for one time step */
/* Input: data[t%2], Output: data[(t+1)%2] */
int accCalc(int nt)
{
    int t, x, y;
#pragma acc data copy(data[0:2][0:NY][0:NX])
//#pragma acc loop seq
    for (t = 0; t < nt; t++) {
        int from = t%2;
        int to = (t+1)%2;

#if 1
        printf("step %d\n", t);
        //fflush(0);
#endif

#pragma acc kernels
#pragma acc loop independent
        for (y = 1; y < NY-1; y++) {
#pragma acc loop independent
            for (x = 1; x < NX-1; x++) {
                data[to][y][x] = 0.2 * (data[from][y][x]
                                        + data[from][y][x-1]
                                        + data[from][y][x+1]
                                        + data[from][y-1][x]
                                        + data[from][y+1][x]);
            }
        }
    }

    return 0;
}


int ompCalc(int nt)
{
    int t, x, y;

    for (t = 0; t < nt; t++) {
        int from = t%2;
        int to = (t+1)%2;

#if 1
        printf("step %d\n", t);
        //fflush(0);
#endif
#pragma omp parallel private(x)
#pragma omp for    
        for (y = 1; y < NY-1; y++) {
            for (x = 1; x < NX-1; x++) {
                data[to][y][x] = 0.2 * (data[from][y][x]
                                        + data[from][y][x-1]
                                        + data[from][y][x+1]
                                        + data[from][y-1][x]
                                        + data[from][y+1][x]);
            }
        }
    }

    return 0;
}

int seqCalc(int nt)
{
    int t, x, y;

    for (t = 0; t < nt; t++) {
        int from = t%2;
        int to = (t+1)%2;
        printf("step %d\n", t);
        //fflush(0);
        for (y = 1; y < NY-1; y++) {
            for (x = 1; x < NX-1; x++) {
                data[to][y][x] = 0.2 * (data[from][y][x]
                                        + data[from][y][x-1]
                                        + data[from][y][x+1]
                                        + data[from][y-1][x]
                                        + data[from][y+1][x]);
            }
        }
    }

    return 0;
}

double speed(int nt, int (*function)(int))
{
    struct timeval t1, t2;

    init();

    gettimeofday(&t1, NULL);

    function(nt);

    gettimeofday(&t2, NULL);

    double us;
    double gflops;
    int op_per_point = 5; // 4 add & 1 multiply per point

    us = get_elapsed_time(&t1, &t2);
    gflops = ((double)NX*NY*nt*op_per_point)/us/1000.0;

    return gflops;
}

double seqSpeed(int nt){
    return speed(nt, seqCalc);
}

double ompSpeed(int nt){
    return speed(nt, ompCalc);
}

double accSpeed(int nt){
    return speed(nt, accCalc);
}

int main(int argc, char *argv[]){
    int nt = 20; /* number of time steps */
  
    if (argc >= 2) { /* if an argument is specified */
        nt = atoi(argv[1]);
    }
    double seq=seqSpeed(nt);
    double omp=ompSpeed(nt);
    double acc=accSpeed(nt);
    printf("Sequential Speed: %.3lf GFlops\n", seq);
    printf("OMP Speed: %.3lf GFlops\n", omp);
    printf("ACC Speed: %.3lf GFlops\n", acc);
}