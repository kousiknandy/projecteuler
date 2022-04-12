import functools

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def series(x1, x2):
    y1 = x1[0]*x2[1]+x2[0]*x1[1]
    y2 = x1[1]*x2[1]
    y = gcd(y1, y2)
    return (y1//y, y2//y)

def shunt(x1, x2):
    y2 = x1[0]*x2[1]+x2[0]*x1[1]
    y1 = x1[0]*x2[0]
    y = gcd(y1, y2)
    return (y1//y, y2//y)
    

def sh_sh(s1, s2):
    s = set()
    for x1 in s1:
        for x2 in s2:
            s.add(series(x1,x2))
            s.add(shunt(x1, x2))
    return s

@functools.lru_cache(maxsize=None)
def D(n):
    if n == 0: return set()
    if n == 1: return set([(1,1)])
    if n == 2: return set ([(1,1), (2,1), (1,2)])
    s = set()
    for i in range(1,n):
        s |= D(i)
        s |= sh_sh(D(i), D(n-i))
    return s

for i in range(1, 19):
    print(i, len(D(i)))
    
