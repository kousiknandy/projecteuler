import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def sdigs(n):
    c = n % 10
    while n := n // 10:
        c += n % 10
    return c

def step(f, k):
    if f[0] == 0: return (k, 1)
    n = k*f[0] + f[1]
    d = f[0]
    g = gcd(n, d)
    return (n//g, d//g)

def e_cf(start):
    i = start // 3
    d = start % 3
    if d == 2:
        yield 2*(i+1)
        yield 1
    if d == 1:
        yield 1
    while i >= 1:
        yield 1
        yield 2*i
        yield 1
        i -= 1

c = int(sys.argv[1]) - 1
an, ad = 0, 1
for s in e_cf(c):
    if an == 0:
        an = s
        continue
    an, ad = step((an, ad), s)
    # print("  ", an, ad, s)
an, ad = step((an, ad), 2)

print(an, ad, sdigs(an))
