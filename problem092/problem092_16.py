X, K, D = map(int, input().split())
X = abs(X)
point = X % D
q = X // D
ans = 0
if q >= K:
    ans = abs(X-D*K)
elif (K - q) % 2 == 0:
    ans = point
else:
    ans = D-point
print(ans)