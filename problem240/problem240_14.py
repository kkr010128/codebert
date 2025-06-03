N, M = map(int, input().split())
data = [0]*N
solved = [False]*N
for _ in range(M):
    p, S = input().split()
    p = int(p) - 1
    if solved[p] == False and S == "WA":
        data[p] += 1
    if solved[p] == False and S == "AC":
        solved[p] = True

print(sum(solved),sum( x*y for x, y in zip(data, solved)) )
