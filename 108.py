import sys

# use multiple process in parallel to utilize all cpu cores
# for 5 threads, run with args 1000 5 & 1001 5 & ... 1004 5 &
i = start = int(sys.argv[1]) if len(sys.argv) > 2 else 1000
incr = int(sys.argv[2]) if len(sys.argv) > 2 else 1

while True:
    s = 0
    for j in range(i+1, 2*i+1):
        if (i * j) % (j - i) == 0:
            s += 1
        if s >= 1000:
            print(i)
            exit()
            # other processes to be killed manually afterwards
    i += incr
    # if (i-start) % 100000 == 0: print("*")
    # elif (i-start) % 50000 == 0: print("#")
    # elif (i-start) % 1000 == 0: print(".", end="")
    
