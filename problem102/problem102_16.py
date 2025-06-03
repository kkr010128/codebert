def solve(n, k, a):
    for i in range(k, n):
        print("Yes" if a[i-k] < a[i] else "No")

n, k = map(int, input().split())
a = list(map(int, input().split()))
solve(n, k, a)