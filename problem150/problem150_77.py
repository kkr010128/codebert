N, K = map(int,input().split())
As = list(map(int,input().split()))

visited = [0] * N
path = []
now_town = 1
while(True):
    visited[now_town-1] = 1
    path.append(now_town)
    now_town = As[now_town-1]
    if visited[now_town-1] == 1:
        break
index = path.index(now_town)
loop = path[index:len(path)]
loop_len = len(loop)
if index < K:
    k = K - index
    r = k % loop_len
    print(loop[r])
else:
    print(path[K])
