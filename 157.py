# 1/a + 1/b = p/10^n
# 10^n = pab/a+b
#      = pgxy/x+y
#      = gxy = 2^n5^n  [1,2,5,10]  (1,1) (1,2) (1,5) (1,10) (2,5)
# pg = 10^n*2, 10^n*3/2, 10^n*6/5, 10^n*11/10, 10^n*7/10
#    = 2*10^n, 15*10^n-1, 12*10^n-1, 11*10^n-1, 7*10^n-1
#    = 20, 15, 12, 11, 7 (n=1) = 6 + 4 + 6 + 2 + 2 (n=1) = 20
#    = 2^n+1*5^n, 2^n-1*3*5^n, 2^n+1*3*5^n-1, 2^n-1*5^n-1*11, 7*2^n-1*5*n-1
#    = (n+2)(n+1), 2n(n+1), 2n(n+2), 2n^2, 2n^2
#    = n^2+3n+2 + 2n^2+2n + 2n^2+4n + 2n^2 + 2n^2
#    = 9n^2+9n+2
#
# generalized -- a, b: (1, 2^x5^y) 0<=x,y<=n, (2^x, 5^y) 1<=x,y<=n
# solutions are number of factors of pg = 10^n (a+b)/(ab) 

def nfactors(n):
    f = 0
    for d in range(1, 1+int(n**0.5)):
        if n % d == 0:
            f += 1 if d*d == n else 2
    return f

solutions = 0
for n in range(1, 10):
    for x in range(n+1):
        for y in range(n+1):
            a, b = 1, (2**x)*(5**y)
            prod = (10**n) * (a+b) // (a*b)
            solutions += nfactors(prod)
    for x in range(1, n+1):
        for y in range(1, n+1):
            a, b =  (2**x), (5**y)
            prod = (10**n) * (a+b) // (a*b)
            solutions += nfactors(prod)
            
print(solutions)
