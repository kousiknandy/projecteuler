import sys
from operator import mul
from functools import reduce

def fixed_length_partitions(n,L):
    """
    Integer partitions of n into L parts, in colex order.
    The algorithm follows Knuth v4 fasc3 p38 in rough outline;
    Knuth credits it to Hindenburg, 1779.
    """
    
    # guard against special cases
    if L == 0:
        if n == 0:
            yield []
        return
    if L == 1:
        if n > 0:
            yield [n]
        return
    if n < L:
        return

    partition = [n - L + 1] + (L-1)*[1]
    while True:
        yield partition
        if partition[0] - 1 > partition[1]:
            partition[0] -= 1
            partition[1] += 1
            continue
        j = 2
        s = partition[0] + partition[1] - 1
        while j < L and partition[j] >= partition[0] - 1:
            s += partition[j]
            j += 1
        if j >= L:
            return
        partition[j] = x = partition[j] + 1
        j -= 1
        while j > 0:
            partition[j] = x
            s -= x
            j -= 1
        partition[0] = s

start, end = int(sys.argv[1]), int(sys.argv[2])
        
prsums = set()
for k in range(start, end+1):
    f = False
    for n in range(k, k*k+1):
        for x in fixed_length_partitions(n, k):
            pr = reduce(mul, x, 1)
            # print(k, n, pr, x)
            if pr == n:
                # print(">>> ", k, ":", n)
                prsums.add(n)
                f = True
                break
            if pr > n: break
        if f: break
    else:
        print("major bug:", k, "looked upto", n, "giving up")
print(prsums)
