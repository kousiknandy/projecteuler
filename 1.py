f1 = lambda x, y: x*y*(y+1)//2
f2 = lambda x: f1(x,999//x)
f3 = lambda x, y: f2(x) + f2(y) - f2(x*y)
f3(3,5)
# 233168
