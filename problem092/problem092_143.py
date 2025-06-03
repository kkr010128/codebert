import math
X, K, D = map(int, input().split())
ans = 0
if K * D < abs(X):
    ans = abs(X) - K * D
elif (K - math.floor(abs(X) / D)) % 2 == 0:
    ans = abs(X) - (math.floor(abs(X) / D)) * D
else:
    ans = abs(X) - (math.floor(abs(X) / D)) * D - D

print(abs(int(ans)))
