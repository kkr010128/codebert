X, K, D = map(int, input().split())
X = abs(X)
r = X % D
t = X // D
if t >= K:
    ans = abs(X - K * D)
elif (K - t) % 2 == 0:
    ans = r
else:
    ans = D - r
print(ans)