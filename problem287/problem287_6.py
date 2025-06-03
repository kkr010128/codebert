import itertools

N = int(input())

flag = 0

for i, j in itertools.product(range(9), repeat=2):
    if (i + 1) * (j + 1) == N:
        print('Yes')
        flag = 1
        break

if flag == 0:
    print('No')