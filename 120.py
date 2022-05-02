# (a+1)^n = a^n + nC1 a^n-1 + nC2 a^n-2 + .....+ nCn-2 a^2 + nCn-1 a + 1
# (a-1)^n = a^n - nC1 a^n-1 + nC2 a^n-2 - .....+/- nCn-2 a^2 +/- nCn-1 a +/- 1 (depending in n even/odd)
# (a+1)^n + (a-1)^n = 2 a^n + 2 nC2 a^n-2 + ... + 2 nCn-1 a (odd n) = 2 n a mod a^2
#                   = 2 a^n + 2 nC2 a^n-2 + ... + 2 (even n) = 2 mod a^2
# maximize (2*n*a % a*a) for odd n (happens when n = a-1//2, but I didn't know earlier)

s = 0
for a in range(3,1001):
     s += max([(2*a*n)%(a*a) for n in range(1,2*a+1,2)])
print(s) # 333082500
