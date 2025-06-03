n, m = map(int, input().split())
A = list(map(int, input().split()))
s = 0
for i in range(m):
    s += A[i]
if s > n:
    print(-1)
elif s <= n:
    print(n - s)