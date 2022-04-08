import functools

@functools.lru_cache(maxsize=None)
def collatz(n):
    if n in [1, 2]: return n
    if n % 2: return 1 + collatz(3*n + 1)
    return 1 + collatz(n//2)

maxc = 0
maxn = 0
for i in range(1, 10**6+1):
    c = collatz(i)
    if c > maxc:
        maxc = c
        maxn = i
print(maxn)
