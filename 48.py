def xtox(x):
    a = 1
    for i in range(1, x+1):
        a *= x
        a %= 10**10
    # print(x, a)
    return a

sum = 0
for i in range(1, 1001):
    sum += xtox(i)
    sum %= 10**10
print(sum)
