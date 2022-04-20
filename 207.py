# looking for real solution vs integer solution ratio for <=k
# for the equation 4^t = 2^t + k, where 2^t and k are integers
# so we need diophantine solutions to x^2 - x - y = 0 which has
# generating functions per https://www.alpertron.com.ar/QUAD.HTM
#      x = 2k+1, y = 4k^2+2k and x = 2k+2, y = 4k^2+6k+2
# now for all y this produces real solutions but integer solutions
# are when 2k+2 is a power of 2 (so k+1 is 2^p). So we count real
# solutions and integer solutions till their ratio is < 1/12345.

n_m = 0  # integer solution count
d_m = -1 # real solution count, skip the first 0 as solution
for k in range(104944): # this is arbitrary
    y = 4*k*k+2*k
    d_m += 1
    # print(y, " (",n_m,"/",d_m,")", sep="")
    if 12345*n_m < d_m: break
    if bin(k+1).count("1") == 1: n_m += 1 # k+1 = 2^p
    y = 2*(2*k*k+3*k+1)
    d_m += 1
    # print(y, " (",n_m,"/",d_m,")", sep="")
    if 12345*n_m < d_m: break
print(y)
