CC = pgcc
#CFLAGS = -O2 -acc -mp
CFLAGS = -O2 -acc -mp -Minfo=accel
LDFLAGS = -acc -mp
LIBS = 

APP = diffusion
OBJS = $(APP).o

all: $(APP)

$(APP): $(OBJS)
	$(CC) $^ $(LIBS) -o $@ $(LDFLAGS)

%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $*.o

clean:
	rm -f *.o
	rm -f $(APP)
	rm -f *~
