A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.insert(0, 10**6)
b.insert(0, 10**6)
xyc = [list(map(int, input().split())) for _ in range(M)]

ans = min(a) + min(b)

for n in xyc:
    ans = min(ans, a[n[0]] + b[n[1]] - n[2])

print(ans)