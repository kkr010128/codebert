X, K, D = map(int, input().split())
X = abs(X)
if X // D <= K:
    print(min(abs(X % D - (K - (X // D))%2*D), abs(X % D + (K - (X // D))%2*D)))
else:
    print(min(abs(X - K*D), abs(X + K*D)))
