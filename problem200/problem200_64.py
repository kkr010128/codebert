A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 10**9

for i in range(M):
    x, y, c = map(int, input().split())
    if ans > a[x-1] + b[y-1] - c:
        ans = a[x-1] + b[y-1] - c

if min(a) + min(b) < ans:
    ans = min(a) + min(b)

print(ans)
