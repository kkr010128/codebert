N = int(input())
A = list(map(int, input().split()))
if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
elif A[0] != 0:
    print(-1)
    exit()

leaf = A
not_leaf = [0] * (N + 1)
not_leaf[0] = 1

for i, a in enumerate(A[1:-1], 1):
    not_leaf[i] = not_leaf[i - 1] * 2 - a

for i in reversed(range(1, N + 1)):
    total = not_leaf[i] + leaf[i]
    prev = not_leaf[i - 1]
    if prev > total:
        not_leaf[i - 1] -= prev - total
    if not_leaf[i - 1] * 2 < total:
        print(-1)
        break
else:
    print(sum(leaf) + sum(not_leaf))