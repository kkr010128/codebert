A, B, M = map(int, input().split())
a = [int(a) for a in input().split()]
b = [int(b) for b in input().split()]
X = [0] * M
Y = [0] * M
C = [0] * M
for i in range(M):
    X[i], Y[i], C[i] = map(int, input().split())

all_prices = []
for x, y, c in zip(X, Y, C):
        all_prices.append(a[x-1] + b[y-1] - c)

prices = [min(a) + min(b), min(all_prices)]

print(min(prices))