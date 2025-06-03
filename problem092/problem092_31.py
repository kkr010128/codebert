X, K, D = [int(x) for x in input().split()]

X=abs(X)
s = min(K, X//D)
K = K - s
X = X - s*D
#print(s, K, X)
if K%2 == 0:
    print(X)
else:
    print(D-X)