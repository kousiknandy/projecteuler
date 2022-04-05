import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

maxn = 0
maxab = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1000):
        for n in range(1000):
            p = n * n + a * n + b
            if p in primeset: continue
            if n > maxn:
                maxn = n
                maxab = a * b
            break
print(maxab)
