from itertools import product
h, w, k = map(int, input().split())
c = [[1 if j == '#' else 0 for j in input()] for i in range(h)]
cnt = 0
for br in product([0, 1], repeat=h):
    for bc in product([0, 1], repeat=w):
        if sum(c[i][j]*br[i]*bc[j] for i, j in product(range(h), range(w))) == k:
            cnt += 1
print(cnt)