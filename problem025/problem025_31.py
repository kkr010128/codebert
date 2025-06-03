aN = int(input())
A = list(map(int, input().split()))
mN = int(input())
M = list(map(int, input().split()))

def memorize(f) :
    cache = {}
    def helper(*args) :
        if args not in cache :
            cache[args] = f(*args)
        return cache[args]
    return helper

@memorize
def solve(i, m):
    if m == 0:
        return True
    if i >= aN:
        return False
    
    res = solve(i + 1, m) or solve(i + 1, m - A[i])
    return res

for m in M:
    print("yes" if solve(0, m) else "no")
