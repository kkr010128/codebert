N = int(input())
X = list(map(int, input().split()))

HP = []
for p in range(1, 101, 1):
    P = [p] * len(X)
    delta = sum([(i - j) ** 2 for (i, j) in zip(X, P)])
    HP.append(delta)

print(min(HP))
