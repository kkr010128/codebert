A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c0 = min(a) + min(b)
for i in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    cnext = a[x] + b[y] - c
    c0 = min(c0, cnext)
print(c0)