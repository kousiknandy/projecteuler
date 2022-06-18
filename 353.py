import functools
import itertools
import math

def psieve():
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step

maxlim = 2**15
primes = []
for p in psieve():
    if p > int(maxlim**0.5): break
    if p % 4 == 3:
        primes.append(p)

def squarable(num):
    if num <= 2: return True
    for p in primes:
        c = 0
        while num % p == 0:
            c += 1
            num //= p
        if c % 2: return False
        if p > num: break
    return True

# print([x for x in range(2, 1000) if  squarable(x)])

r = 7

def stns(r):
    for x in range(r+1):
        c = r*r - x*x
        #print(x,c)
        if squarable(c):
            for y in range(int(c**0.5)+1):
                # print(x,c,y)
                zq = c - y*y
                z = int(zq**.5 +.5)
                if c == y*y + z*z:
                    yield x, y, z
                    if z:
                        yield x, y, -z 

# for s in stns(7): print(s)

def dist(a, b, r):
    return r * math.acos((a[0]*b[0]+a[1]*b[1]+a[2]*b[2])/(r*r))

def risk(a, b, r):
    return (dist(a, b, r)/(math.pi*r))**2

# print(dist((0,0,1),(0,0,-1),1))
# print(risk((0,0,1),(0,1,0),1), risk((0,1,0),(0,0,-1),1))

def station_risks(radius):
    stations = list(stns(radius))
    ns = len(stations)
    risks = [None for _ in range(ns)]
    for r in range(ns): risks[r] = [0.0 for _ in range(ns)]
    for r in range(ns):
        for c in range(r+1,ns):
            if r != c:
                risks[r][c] = risks[c][r] = risk(stations[r],  stations[c], radius)
    return risks, ns

# print(stations)
# for r in risks: print(r)

def floyd_warsall(risks, sz):
    dist = risks # map(lambda i : map(lambda j : j , i) , risks) 
    for k in range(sz):
        for i in range(sz):
            for j in range(sz):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

s = 0.0
for m in range(1, 16):
    risks, ns = station_risks(2**m-1)
    shortests = floyd_warsall(risks, ns)
    # for r in shortests: print(r)
    print(2**m-1, ns, shortests[0][1])
    s += (shortests[0][1])

print(s)
