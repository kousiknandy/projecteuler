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

d = int(600851475143 ** 0.5)
m = prime_search(d, nearest=True)
for i in range(m, -1, -1):
    if 600851475143 % primes[i] == 0:
        print(primes[i])
        break
else:
    print("600851475143 is prime")
