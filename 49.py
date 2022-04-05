from functools import reduce
import itertools
import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

def prime_search(num, nearest=False, primes=primes, primeset=primeset):
    if not nearest and num not in primeset: return -1
    l = 0
    r = len(primes) - 1
    while l <= r:
        m = (l + r) // 2
        if primes[m] == num or l == r: return m
        if primes[m] < num:
            l = m + 1
        else:
            r = m - 1
    return l

def digits(n):
    while n:
        yield n % 10
        n //= 10

def permutations(p):
    d = list(digits(p))
    for x in itertools.permutations(d):
        yield reduce(lambda x, y: 10 * x + y, x)

def samedigits(p1, p2):
    d1 = list(digits(p1))
    d2 = list(digits(p2))
    d1.sort()
    d2.sort()
    return d1 == d2
        
l = prime_search(1000, nearest=True)
r = prime_search(10000, nearest=True)
primes = primes[l+1:r+1]
primeset = frozenset(primes)

for p1 in primes:
    for p2 in permutations(p1):
        if p2 <= p1 or p2 not in primeset: continue
        p3 = p2 + (p2 - p1)
        if p3 in primeset and samedigits(p3, p1):
            res = p1 * 10**8 + p2 * 10**4 + p3
            print(res)
            if p1 != 1487:
                exit()
