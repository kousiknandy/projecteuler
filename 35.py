from functools import reduce
import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

def digits(n):
    while n:
        yield n % 10
        n //= 10

def circulars(p):
    d = list(digits(p))[::-1]
    for i in range(len(d)):
        n = reduce(lambda x, y: 10 * x + y, d)
        yield n
        d = d[1:] + [d[0]]

count = 0
for p in primes:
    for n in circulars(p):
        if n not in primeset: break
    else:
        count += 1
print(count)

        
