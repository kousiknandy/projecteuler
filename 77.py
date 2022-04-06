import functools
import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]

@functools.lru_cache(maxsize=None)
def combinations(num, idx=0):
    if num == 0:
        return 1
    if num < 0:
        return 0
    com = 0
    while True:
        if primes[idx] > num:
            break
        com += combinations(num - primes[idx], idx)
        idx += 1
    return com

num = 2
while True:
    com = combinations(num)
    if com >= 5000:
        print(num)
        break
    num += 1
