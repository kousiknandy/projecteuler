from functools import reduce

def digits(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    return d[::-1]

def palindrome(p):
    d1 = digits(p)
    d2 = d1[::-1]
    return d1 == d2

def rev_add(n):
    d1 = digits(n)[::-1]
    x = 0
    for d in d1:
        x = x*10 + d
    return x+n

s = 0
lychrel = [False] * 10_000
for l in range(10, 10001):
    n = rev_add(l)
    q = [l, n]
    i = 1
    while True:
        if n < len(lychrel) and lychrel[n]: break
        if i >= 50: break
        if palindrome(n): break
        i += 1
        n = rev_add(n)
        q.append(n)
    if i < 50:
        for j in q:
            if j < len(lychrel):
                lychrel[j] = True
    else:
        s += 1

print(s)
