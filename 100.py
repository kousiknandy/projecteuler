# https://www.alpertron.com.ar/QUAD.HTM
# x(n+1) = 3x(n) + 2⁢y(n) - 2
# y(n+1) = 4x(n) + 3y(n) - 3⁢

x, y = 15, 21
while y < 10**12:
    x, y = 3*x+2*y-2, 4*x+3*y-3
print(x)
