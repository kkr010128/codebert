A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 999999

for i in range(M):
    x, y, c = map(int, input().split())
    if x <= A and y <= B:
        d = a[x - 1] + b[y - 1] - c
        if d < ans:
            ans = d

if (min(a) + min(b)) < ans:
    ans = min(a) + min(b)

print(ans)