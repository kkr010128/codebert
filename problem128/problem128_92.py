
X, N = map(int, input().split())
P = list(map(int, input().split()))

occupied = set(P)
for i in range(200):
    if X - i not in occupied:
        print(X - i)
        break

    if X + i not in occupied:
        print(X + i)
        break
