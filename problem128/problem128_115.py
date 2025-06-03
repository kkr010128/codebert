X, N = map(int, input().split())
P = set(map(int, input().split()))

d = 10 ** 9
ans = 0
for i in range(120):
    if (i in P):
        continue
    if (abs(X - i) < d):
        ans = i
        d = abs(X - i)
print(ans)