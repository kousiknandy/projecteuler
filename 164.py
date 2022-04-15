import functools

# use the dynamic programming + memoization
# f(d1, d2, remaining_length) = Σ f(d2, d3, remaining_length-1)
#                               d3 = 0 to 9-d1-d2
@functools.lru_cache(maxsize=None)
def numbers(last2, n):
    t = s = 0
    if not last2:
        s = 1 # the first digit must be non zero
        last2 = (0, 0)
    c = 10-last2[0]-last2[1] 
    if n:
        for d in range(s,c):
            t += numbers((last2[1], d), n-1)
    else:
        t = c
    return t

# print(numbers(None,1))
# print(numbers(None,2))
# print(numbers(None,3))
# print(numbers(None,4))
print(numbers(None,19))
