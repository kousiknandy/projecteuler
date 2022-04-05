import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

def truncated(p):
    i = 0
    n = p
    while n > 0:
        yield n
        n //= 10
        i += 1
    n = p
    while i > 0:
        yield n % (10 ** i)
        i -= 1

sum = 0
count = 0
for p in primes:
    if p <= 7: continue
    for x in truncated(p):
        if x not in primeset:
            break
    else:
        sum += p
        count += 1
        if count == 11:
            break
print(sum, count)
