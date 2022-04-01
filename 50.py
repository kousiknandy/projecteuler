import sys
# read all primes (pre-calculated) to a million
with open(sys.argv[1]) as p_file:
    primes = p_file.read()
primes = primes.split(",")
primes = [int(x) for x in primes]
primeset = frozenset(primes)
# sum of 546 smallest primes exceeds a million,
# so that can be biggest sliding window size
m, v = 0, 0
for window in range(546, 1, -1):
    wsum = sum(primes[:window])
    if wsum in primeset: v, m = wsum, window
    # keep sliding the window till sum exceeds
    for st in range(1,len(primes)):
        wsum += primes[st+window-1] - primes[st-1]
        if wsum > 10**6: break
        if wsum in primeset:v, m = wsum, window
    if v: break
print(v, m)
