N, K = map(int, input().split())
p = list(map(int, input().split()))

cost = 0
for i in range(K):
    cost += min(p)
    p.remove(min(p))
print(cost)