import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

def prime_factors(n):
    i = 0
    f = set()
    while primes[i]**2 <= n:
        if n % primes[i]:
            i += 1
        else:
            n //= primes[i]
            f.add(primes[i])
    if n > 1: f.add(n)
    return len(f)

i = 2
while True:
    for j in range(4):
        if prime_factors(i+j) != 4:
            break
    else:
        print(i)
        break
    i += 1
