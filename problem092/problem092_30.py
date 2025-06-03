X, K, D = map(int, input().split())
X = abs(X)
q, m = divmod(X, D)
if q >= K:
    print(X-K*D)
elif (q+K)%2==0:
    print(m)
else:
    print(-(m-D))
