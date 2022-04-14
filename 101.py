# given a polynomial `un` we need to slowly (one degree at a time) derive the same
# which means, approximate it by a 0 degree polynomial, find the first fail then
# approximate by 1 degree polynomial again find the first fail, accumulate fails.
# assume original function is fn=n^3 and hence the expected values are 1,8,27,64...
# given 1, we guess fn = 1, so f(1) matches but f(2) fails as 1!=8 so we have bop=1
# given 1,8 we guess fn = -6+7n, f(1) and f(2) matches but f(3)=15 fails so bop=15 
# given 1,8,27 we guess fn=6-11n+6n^2, f(1),f(2),f(3) matches, f(4)=58 becomes bop
# given 1,8,27,64 we finally guess fn=n^3 hence the accumulated bop=1+15+58=74

# assume fn(x) = c0 + c1*x + c2*x^2 + ... + cn*x^n, and we're given fn(1),fn(2) etc
# so we solve simultaneous equations like
# c0 + c1 + c2 + c3 + ... = fn(1)
# c0 + 2*c1 + 4*c2 + ...  = fn(2)
# c0 + 3*c1 + 9*c2 + ...  = fn(3)
def gen_poly(degree):
    pol = [None] * degree
    for i in range(degree):
        pol[i] = [(i+1)**j for j in range(degree)]
    return pol

# so we create an augmented matrix and solve by Gaussian-Jordan elimination method
# [1  1  1  1]
# [1  2  4  8]
# [1  3  9 27]
def gauss_jordan(degree, fx):
    # generate the coefficients and add the solution as last column
    coff = gen_poly(degree)
    for d in range(degree):
        coff[d].append(fx[d])
    # first triangulate the matrix, zeroise everything left of diagonal 
    for i in range(degree):
        # zeroise the ith column from i+1th row onwards
        for j in range(i+1, degree):
            y = coff[j][i]/coff[i][i]
            for k in range(i, degree+1):
                coff[j][k] += -y*coff[i][k]
    # then run it backwards, zeroise everything right of diagonal
    for i in range(degree-1, -1, -1):
        y = coff[i][i]
        # scale the row first to have 1 as diagonal
        for k in range(i,degree+1):
            coff[i][k] /= y
        for j in range(i-1, -1, -1):
            y = coff[j][i]
            for k in range(i, degree+1):
                coff[j][k] += -y*coff[i][k]
    # the result is left in the last column of the matrix
    # [1  0  0  6]
    # [0  1  0 -11]
    # [0  0  1  6]
    return [x[degree] for x in coff] 

un = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
u = [un(n) for n in range(1,20)]
sbop = 0
fn = lambda f, n: sum(x[0]*n**x[1] for x in zip(f, range(len(f))))
for k in range(1,11):
    # find the polynomial that fits the first k elements
    f = gauss_jordan(k, u[:k])
    # find the first misfit, remember accidentally a lower degree approximation
    # may get more than the given terms correct but usually f(k+1) is the bop
    for i in range(1,k+2):
        bop = fn(f,i)
        if bop != u[i-1]:
            sbop += bop
            break
print(sbop)
