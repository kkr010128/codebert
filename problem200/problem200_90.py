A, B, M = map(int, input().split())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))

prm_min = min(la) + min(lb)

lcost = list()
for i in range(M):
    x, y, c = map(int, input().split())
    lcost.append(la[x-1] + lb[y-1] - c)

print(min(min(lcost), prm_min))