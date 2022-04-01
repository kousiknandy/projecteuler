import sys
# read all primes (pre-calculated) to a million
with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)
sumof = [0] * len(primes)
# sum of 546 smallest primes exceeds a million,
# so that can be biggest sliding window size
for window in range(546, 1, -1):
    wsum = sum(primes[:window])
    if wsum in primeset:
        idx = primes.index(wsum)
        sumof[idx] = max(sumof[idx], window)
    # slide the window till the sum exceeds
    for st in range(1,len(primes)):
        wsum -= primes[st-1]
        wsum += primes[st+window-1]
        if wsum > 10**6: break
        if wsum in primeset:
            idx = primes.index(wsum)
            sumof[idx] = max(sumof[idx], window)
    if any(sumof):
        break
m, v = 0, 0
for j in range(len(primes)-1, -1, -1):
    if sumof[j] > m:
        m = sumof[j]
        v = primes[j]
print(v, m)

