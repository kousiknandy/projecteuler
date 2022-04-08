import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]

primearray = [True] * 2 * 10**6
maxf = int((2 * 10**6) ** 0.5)
i = 0
while primes[i] <= maxf:
    j = 2 * primes[i] 
    while j < len(primearray):
        primearray[j] = False
        j += primes[i]
    i += 1
finalprimes = [i for i in range(len(primearray)) if primearray[i]]
print(sum(finalprimes)-1)
