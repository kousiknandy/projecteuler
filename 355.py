import functools
import itertools

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

maxlim = 100 #200000
primes = []
for p in psieve():
    if p > int(maxlim**0.5): break
    primes.append(p)

facts = frozenset()

def coprime(num, factors):
    f = set()
    if num in factors: return None
    for p in primes:
        if p*p > num: break
        while num % p == 0:
            f.add(p)
            f.add(num//p)
            if p in factors or (num//p) in factors:
                return None
            p *= p
            if p >= num: break
    f.add(num)
    return f

@functools.lru_cache(maxsize=None)
def maxsum(currsum, num, factors):
    # print(" "*d, currsum, num, factors)
    if num == 1: return currsum+1
    while (f := coprime(num, factors)) is None:
        #print(num)
        num -= 1
        if num == 1: break
    if num == 1: return currsum+1
    factors2 = factors | f
    s1 = maxsum(currsum+num, num-1, factors2)
    s2 = maxsum(currsum, num-1, factors)
    return max(s1, s2)

print(maxsum(0, maxlim, facts))
