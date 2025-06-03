n = int(input())
X = []
Y = []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x+y)
    Y.append(x-y)

a, b, c, d = max(X), min(X), max(Y), min(Y)
print(max(abs(a-b), abs(c-d)))
