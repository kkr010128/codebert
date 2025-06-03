def solve(n, k, s):
    a = [1 if s == 10**9 else s+1] * n
    for i in range(k):
        a[i] = s
    return " ".join(map(str, a))

n, k, s = map(int, input().split())
print(solve(n, k, s))