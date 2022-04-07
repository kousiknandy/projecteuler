
def digits(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    return d

def pandigital(l):
    l.sort()
    return l == list(range(1,10))

fN = 1
fN1 = 1
n = 2
while True:
    fN2 = fN1 + fN
    n += 1
    d = digits(fN2 % 10**9) # first try last 9 so we can give up faster
    if len(d) == 9 and pandigital(d):
        d = digits(fN2) # looks promising so try the full test
        if pandigital(d[:9]) and pandigital(d[-9:]):
            print(n)
            break
    fN = fN1
    fN1 = fN2
