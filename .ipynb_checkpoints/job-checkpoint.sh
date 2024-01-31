#!/bin/sh
#$ -cwd
#$ -l q_node=1
#$ -l h_rt=00:10:00

pgcc -acc -mp -shared -o diffusion.so diffusion.c