h,w = map(int,input().split())

f = []
for i in range(h):
    s = list(map(lambda x:0 if x== "." else 1,list(input())))
    f.append(s)

from collections import deque
def dfs_field(field,st,go):
    """
    :param field: #が1,.が0になったfield
    st: [i,j]
    go: [i,j]
    :return: 色々今は回数returnしている。
    """
    h = len(field)
    w = len(field[0])
    around = [[-1,0],[1,0],[0,1],[0,-1]]
    que = deque()
    visited = set()
    visited.add(str(st[0])+","+str(st[1]))
    que.append([st[0],st[1],0])
    max_cos = 0
    while True:
        if len(que) == 0:
            return  max_cos
        top = que.popleft()
        nowi = top[0]
        nowj = top[1]
        cost = top[2]
        for a in around:
            ni = nowi+a[0]
            nj = nowj+a[1]
            if ni < 0 or ni > h-1 or nj < 0 or nj > w-1:
                continue
            if field[ni][nj] == 1:
                continue
            if ni == go[0] and nj == go[1]:
                return cost+1
            else:
                key = str(ni)+","+str(nj)
                if key not in visited:
                    que.append([ni,nj,cost+1])
                    visited.add(key)
                    if cost+1 > max_cos:
                        max_cos = cost+1
        # print(que)



ans = 0
for i in range(h):
    for j in range(w):
        if f[i][j] == 0:
            ct = dfs_field(f,[i,j],[-2,-2])
            if ans < ct:
                ans = ct

print(ans)

