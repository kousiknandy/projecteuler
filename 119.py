from math import log

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

i = 1
n = 10
s = 1
while True:
    n += 1
    s = s+1 if n%10 else sum_digits(n)
    if s == 1 or s%9 != n%9: continue
    p = log(n)/log(s)
    if abs(p - int(p+0.5)) < 0.000001:
        if s ** int(p+0.5) == n:
            print(i, int(p+0.5), s, s%9,  n, n%9)
            if i == 30: break
            i += 1
