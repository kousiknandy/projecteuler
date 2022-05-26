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

primes = []
for p in psieve():
    if p > 15746722: break
    primes.append(p)
        
@functools.lru_cache(maxsize=None)
def n_k(n, k):
    if n < k: return 0
    if n == 1 or k == 0: return 1
    if k == 1: return n
    if k == n: return 1
    return n_k(n-1, k) + n_k(n-1, k-1)

@functools.lru_cache(maxsize=None)
def squarefree(n):
    for p in primes:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return False
        if p*p > n: break
    return True

rows = 51
coffs = set()
for n in range(rows):
    for k in range(n+1):
        nk = n_k(n, k)
        if squarefree(nk):
            coffs.add(nk)

print(sum(coffs))   # 34029210557338
