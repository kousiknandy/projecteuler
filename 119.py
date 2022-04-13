
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

res = []
for iteration in range(2):
    for num in range(iteration*1000+1, (iteration+1)*1000+1):
        v = num
        if v <= 1: continue
        for pow in range(1, 100):
            v *= num
            if sum_digits(v) == num:
                res.append(v)
                #print(iteration, num, pow+1, num**(pow+1), v)

print(sorted(res)[30])

