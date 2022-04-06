def digits(n):
    while n:
        yield n % 10
        n //= 10

def samedigits(p1, p2):
    d1 = list(digits(p1))
    d2 = list(digits(p2))
    d1.sort()
    d2.sort()
    return d1 == d2

c = 1
while True:
    if all([samedigits(c, x*c) for x in range(2,7)]):
        print(c)
        break
    c += 1
