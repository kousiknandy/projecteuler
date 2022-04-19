def palindrome(num):
    p, n = 0, num
    while n:
        p = p * 10 + n % 10
        n //= 10
    return num == p

sum_sq = lambda x: x * (x+1) * (2*x+1) // 6
palins = set() # some numbers will be sum of squares in multiple ways
for i in range(10**4):
    for j in range(i+2, 10**4+1):
        to_i = sum_sq(i)
        to_j = sum_sq(j)
        diff = to_j - to_i
        if diff > 10**8: break
        if palindrome(diff):
            palins.add(diff)

print(sum(palins))
