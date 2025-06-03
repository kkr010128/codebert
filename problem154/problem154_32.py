from collections import defaultdict

N, K = map(int, input().split())

d = {i: [] for i in range(1, N+1)}
for _ in range(K):
    candy = int(input())
    for i in map(int, input().split()):
        d[i].append(candy)

print(list(d.values()).count([]))
