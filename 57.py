def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def digs(n):
    c = 1
    while n := n // 10:
        c += 1
    return c

def step(f, k=2):
    n = k*f[0] + f[1]
    d = f[0]
    g = gcd(n, d)
    return (n//g, d//g)

s = (2,1)
c = 0
for i in range(1000):
    an, ad = step(s, 1)
    if digs(an) > digs(ad): c+= 1
    s = step(s)
print(c)
