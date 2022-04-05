import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

for n in range(9, 10**6, 2):
    if n in primeset: continue
    for i in range(int((n/2)**0.5)+1):
        p = n - 2*i*i
        if p in primeset: break
    else:
        print(n)
        break
