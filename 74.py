factorials = [1]
f = 1
for i in range(1, 10):factorials.append(f := f*i)

def sum_factdigits(n):
    s = 0
    while n:
        s += factorials[n % 10]
        n //= 10
    return s

unique_loop = [None] * 10**6
for num in range(10**6):
    chain = [num]
    while num >= 10**6 or unique_loop[num] is None:
        # print(num, end=",")
        num = sum_factdigits(num)
        try:
            l = chain.index(num)
            # print("loop (",l,")", num, end=" ")
            for i, n in enumerate(chain):
                if n < 10**6-1:
                    unique_loop[n] = (len(chain)-i) if i < l else (len(chain)-l)
            break
        except:
            chain.append(num)
    else:
        l = unique_loop[num]
        # print("cache (",l,")", num, end=" ")
        for i, n in enumerate(chain):
            if n < 10**6-1:
                unique_loop[n] = l + len(chain) - i - 1
    # print("::", unique_loop[chain[0]])

n = 0
for k in unique_loop:
    if k == 60: n += 1
    
print(n)
            
