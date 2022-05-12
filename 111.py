from collections import Counter
import heapq

def psieve():
    import itertools
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

def digits(n):
    while n:
        yield n % 10
        n //= 10

d = 10
heaps = [[] for _ in range(10)]
for p in psieve():
    if p < 10**(d-1): continue
    if p > 10**(d): break
    c = Counter(digits(p))
    for dig in c:
        heapq.heappush(heaps[dig], (-c[dig], p))
s = 0
for i,h in enumerate(heaps):
    print("\n", i, end=": ")
    m, p = heapq.heappop(h)
    print(p, end=", ")
    s += p
    m1, p = heapq.heappop(h)
    while m == m1:
        print(p, end=", ")
        s += p
        m1, p = heapq.heappop(h)
print(s)
