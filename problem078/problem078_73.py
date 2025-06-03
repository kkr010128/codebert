MOD = 10**9+7
def mod(x):
    return x % MOD

def solve(n):
    """
    0: {}
    1: {0}
    2: {9}
    3: {0,9}
    """
    x = [1,0,0,0]
    for i in range(n):
        x = list(map(mod, (
            8*x[0],
            (9*x[1] + x[0]),
            (9*x[2] + x[0]),
            (10*x[3] + x[2] + x[1])
        )))
    return x[3]

n = int(input())
print(solve(n))