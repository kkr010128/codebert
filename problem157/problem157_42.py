from collections import Counter
N = int(input())
A = list(map(int, input().split()))
X, Y = [], []
for i in range(N):
    X.append(i + 1 + A[i])
    Y.append(i + 1 - A[i])
XL = Counter(X)
c = 0
for y in Y:
    c += XL.get(y, 0)
print(c)