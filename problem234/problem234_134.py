from itertools import product

n = int(input())

n_num = [[0] * 10 for _ in range(10)]

for i in range(n + 1):
    a, b = int(str(i)[0]), i % 10
    n_num[a][b] += 1

answer = sum(n_num[a][b] * n_num[b][a] for a, b in product(range(1, 10), repeat=2))
print(answer)
