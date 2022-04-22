# this is brute force and will take 1/2 day to run, needs optimization
def factors(n):
    yield 1, n
    s = 1 + n % 2
    if n % 2 == 0: yield 2, n//2
    for f in range(3, int(n**0.5+0.5)+1, s):
        if n % f == 0: yield f, n//f
s = 0
for n1 in range(1, 50*10**6):
    f = set()
    for f1, f2 in factors(n1):
        if 3*f2 > f1 and (f1+f2) % 4 == 0 and (5*f2+f1) % 4 == 0:
            n = (5*f2+f1)//4
            k = (f1+f2)//4
            f.add((n,k))
            if len(f) > 1: break
        f1, f2 = f2, f1
        if 3*f2 > f1 and (f1+f2) % 4 == 0 and (5*f2+f1) % 4 == 0:
            n = (5*f2+f1)//4
            k = (f1+f2)//4
            f.add((n,k))
            if len(f) > 1: break
    if len(f) == 1:
        print( n1, end=",")
        s += 1
print("\n",s)
