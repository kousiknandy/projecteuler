def primes6(n):
    r = [False, True] * (n//2) + ([True] if n%2 else [False])
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    return r

def long_divisible(p):
    remainders = set()
    numerator = 1
    d = 1
    while True:
        while numerator < p:
            numerator = numerator * 10 + 1
            d += 1
        remainder = numerator % p
        if remainder == 0:
            # so p divides 11..1 (d digits), does
            # it divide 11....1 (10^9 digits)?
            return 10**9 % d == 0
        if remainder in remainders:
            # results in recurring decimal
            return False
        remainders.add(remainder)
        numerator = remainder

c = 0
s = 0
primes = primes6(5*10**8) # 160001 is sufficient though
primes = [i for i,v in enumerate(primes) if v]

for p in primes:
    if long_divisible(p):
        print(p, end=", ")
        c += 1
        s += p
        if c >= 40: break
else:
    raise RuntimeError("Ran out of primes! Found %d so far" % (c))
print(s)
