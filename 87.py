import sys

with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)

maxsum = 50*10**6
nums = set()
for x2 in primes:
    if x2 >= 7072: break
    for x3 in primes:
        if x3 >= 369: break
        for x4 in primes:
            if x4 >= 84: break
            s = x2**2 + x3**3 + x4**4
            if s > maxsum: continue
            nums.add(s)
print(len(nums))
