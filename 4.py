def digits(n):
    while n:
        yield n % 10
        n //= 10

def palindrome(p):
    d1 = list(digits(p))
    d2 = d1[::-1]
    return d1 == d2

maxprod = 0
for i in range(999, -1, -1):
    for j in range(i, -1, -1):
        if palindrome(i*j):
            maxprod = max(maxprod, i*j)
print(maxprod)
