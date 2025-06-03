



def chebyshev_0(a, b):
    return a - b
def chebyshev_1(a, b):
    return a + b

N = int(input())
X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

max_0 = - (10 ** 9) - 1
min_0 = 2 * (10 ** 9)
for x, y in zip(X, Y):
    if chebyshev_0(x, y) > max_0:
        max_0 = chebyshev_0(x, y)
    if chebyshev_0(x, y) < min_0:
        min_0 = chebyshev_0(x, y)
l0 = abs(max_0 - min_0)

max_1 = - (10 ** 9) - 1
min_1 = 2 * (10 ** 9)
for x, y in zip(X, Y):
    if chebyshev_1(x, y) > max_1:
        max_1 = chebyshev_1(x, y)
    if chebyshev_1(x, y) < min_1:
        min_1 = chebyshev_1(x, y)
l1 = abs(max_1 - min_1)

print(max([l0, l1]))
