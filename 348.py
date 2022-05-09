import sys

def digits(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    return d[::-1]

def palindrome(p):
    d1 = digits(p)
    d2 = d1[::-1]
    return d1 == d2

maxlimit = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8
sumz = [0] * maxlimit

maxof = lambda x, p: int(x**(1/p)+1)
cubes = maxof(maxlimit, 3)
squares = maxof(maxlimit, 2)
for i in range(2, cubes):
    s1 = i**3
    for j in range(2, squares):
        s2 = j**2
        if s1+s2 < maxlimit:
            sumz[s1+s2] += 1
sols = [idx for idx, v in enumerate(sumz) if v == 4]
sols = [s for s in sols if palindrome(s)]
if len(sols) < 5:
    raise RuntimeError("Upper bound %d not sufficient, got %d" % (maxlimit, len(sols)))
print(sols[:5], sum(sols[:5]))
