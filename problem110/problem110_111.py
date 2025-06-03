import itertools
import numpy as np

H, W, K = map(int, input().split())

temp = []
for _ in range(H):
    C = list(input())
    A = [c.replace('.', '0') for c in C]
    A = [a.replace('#', '1') for a in A]
    A = list(map(lambda x: int(x), A))
    temp.append(A)

C = np.array(temp)

count = 0
l = [0, 1]
wide = itertools.product(l, repeat=W)
for w in wide:
    hight = itertools.product(l, repeat=H)
    for h in hight:
        copy_C = C.copy()
        for num, i in enumerate(w):
            if i == 1:
                copy_C[:, num-1] = 0
            for num2, j in enumerate(h):
                if j == 1:
                    copy_C[num2-1, :] = 0
        if copy_C.sum() == K:
            count += 1

print(count)