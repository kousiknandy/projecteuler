import sys

# AF(x) = xF1 + x^2F2 + x^3F3 + X^4F4 + ....
#       = x + x^2 + x^3(F2+F1) + x^4(F3+F2) + ...
#       = x(1 + x + x^2F2 + x^3F3 + ...) + x^2(xF1 + x^2F2 + ...)
#       = x(1 + AF(x)) + x^2AF(x)
# 
# x^2 n + x(1 + n) - n = 0
# x = (-(1+n) +/- √((1+n)^2 +4n^2))/2n
# 
# 5n^2 + 2n + 1 = k^2 <-- perfect square
# n = (-1 +/- √(5k^2-4))/5
#   => 5k^2 - 4 <--- perfect square and √(5k^2-4) - 1 divisible by 5


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

i = 0
q = int(sys.argv[1]) if len(sys.argv)>1 else 2
while True:
    m = ((5*q+1)*(5*q+1)+4)//5
    n = isqrt(m)
    if n * n == m:
        k = n
        j = 5 * k * k - 4
        l = isqrt(j)
        if l * l == j and (l-1) % 5 == 0:
            i += 1
            print((l-1)//5, k, sep=":", end=", ")
            sys.stdout.flush()
            if i == 15:
                print("\n", (l-1)//5)
                break
    q += 1
# warning: does not compute beyond 10th golden nugget
