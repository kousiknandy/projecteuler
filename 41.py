import sys
import itertools
from functools import reduce

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

def digits(n):
    while n:
        yield n % 10
        n //= 10

def pandigital(n):
    d = list(digits(p))
    c = [False] * len(d)
    for x in d:
        try:
            c[x-1] = True
        except IndexError:
            return False
    return all(c)

def isprime(n):
    # if n in primeset: return True
    for p in primes:
        if n % p == 0: return False
    return True

def permutations(p):
    for x in itertools.permutations(p):
        yield reduce(lambda x, y: 10 * x + y, x)

maxpandigital = 0

for l in range(9, -1, -1):
    for x in permutations(range(l, 0, -1)):
        if isprime(x):
            maxpandigital = max(maxpandigital, x)
    if maxpandigital:
        break
print(maxpandigital)
