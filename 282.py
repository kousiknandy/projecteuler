import functools

@functools.lru_cache(maxsize=None)
def ackermann(m, n):
    # print("    ", m, n)
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

# heat up the cache to avoid recursion stack overflow
for i in range(100000):
    ackermann(2, 494*i)
for i in range(500):
    ackermann(3, 494*i)

# but still we won't be able to compute it recursively
s = 0
for i in range(7):
    print(i)
    s += ackermann(i, i)
s %= 14 ** 8
print(s)

# WARNING: does not work
