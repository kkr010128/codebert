K = int(input())
id = 1
cnt = 7
while cnt < K:
    cnt = cnt * 10 + 7
    id += 1

visited = [0] * K
while True:
    remz = (cnt % K)
    if remz == 0:
        break
    visited[remz] += 1
    if visited[remz] > 1:
        id = -1
        break
    cnt = remz * 10 + 7
    id += 1

print(id)
