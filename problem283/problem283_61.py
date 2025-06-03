def solve(n):
    return (n - 1) // 2
assert solve(4) == 1
assert solve(999999) == 499999

n = int(input())
print(solve(n))