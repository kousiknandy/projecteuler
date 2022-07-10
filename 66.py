import functools

@functools.lru_cache(maxsize=1)
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def step(f, k, j):
    n = k*f[1] + f[0]
    d = j*f[1]
    g = gcd(n, d)
    return (d//g, n//g)

def cont_frac(n, s):
    if s == 0:
        print(" "*(10-s),n, 0)
        return (0, 1)
    a = isqrt(n)
    f1 = (2*a, 1)
    f2 = cont_frac(n , s-1)
    f3 = (f1[0]*f2[1]+f1[1]*f2[0], f1[1]*f2[1])
    f4 = ((n-a*a)*f3[1], f3[0])
    g  = gcd(f4[0], f4[1])
    print(" "*(10-s),n, a, s, f1, f2, f3, f4)
    f4 = (f4[0]//g, f4[1]//g)
    return f4

def convergant(n, s):
    a = isqrt(n)
    f1 = (a, 1)
    f2 = cont_frac(n, s)
    f4 = (f1[0]*f2[1]+f1[1]*f2[0], f1[1]*f2[1])
    g  = gcd(f4[0], f4[1])
    return (f4[0]//g, f4[1]//g)
    

for D in range(2, 16):
    a = isqrt(D)
    if a*a == D: continue
    for i in range(10):
        c = convergant(D, i)
        print(D,a, i, c, D**0.5, c[0]/c[1], c[0]*c[0]-D*c[1]*c[1])
    
