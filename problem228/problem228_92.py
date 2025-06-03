from functools import lru_cache
@lru_cache(maxsize=None)
def solve(n):
    if n == 1:
        return 1
    else:
        return solve(n//2) * 2 + 1
H = int(input())
print(solve(H))
