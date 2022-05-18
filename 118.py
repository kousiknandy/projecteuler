import itertools

def digits(n):
    while n:
        yield n % 10
        n //= 10

def repeated(n):
    counts = [0] * 10
    for d in digits(n):
        if d == 0: return True
        counts[d] += 1
        if counts[d] > 1:
            return True
    return False
    
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
    if p > 10**8: break
    if not repeated(p):
        primes.append(p)

def stackdigits(stack):
    ds = []
    for s in stack:
        ds += list(digits(s))
    return sorted(ds)

def complete(stack):
    return stackdigits(stack) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def combos(stack=[], idx=0, depth=0):
    current = stack[:]
    dig = stackdigits(current)
    l = len(dig)
    count = 0
    for i in range(idx, len(primes)):
        if (l + len(list(digits(primes[i])))) > 9:
            break
        for d in digits(primes[i]):
            if d in dig: continue
        new = current + [primes[i]]
        if complete(new):
            count += 1
            # print(" "*depth, new, "*")
            continue
        if len(stackdigits(new)) == 9: continue
        count += combos(new, i+1, depth+1)
    return count

n = combos()
print(n)

