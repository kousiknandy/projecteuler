# the answer is number of prime pairs p1, p2 so that p1*p2 < 10^8
def primes6(n):
    r = [False, True] * (n//2) + ([True] if n%2 else [False])
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5)+1, 2):
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    return r
# generate all primes from 2 ... 10**8/2
p = primes6(5*10**7)
p = [i for i,v in enumerate(p) if v]

com = 0
left = 0
right = len(p)-1
while left < right:
    # squeeze sliding window till first * last < 10^8
    while p[left]*p[right] > 10**8:
        right -= 1
        if left == right: break
    if p[left]*p[right] > 10**8: break
    # print(p[left], p[right], right-left+1)
    # so we have (first, first...last) so last-first+1 pairs
    com += right - left + 1
    left += 1
print(com)
