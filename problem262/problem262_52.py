from collections import defaultdict,deque
n = int(input())
d = defaultdict(list)
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        d[i].append((x-1,bool(y)))
        
maxi = 0
for i in range(2 ** n):
    honest = [-1]*n
    que = deque([])
    for j in range(n):
        if ((i >> j) & 1):
            que.append(n-1-j)
            honest[n-1-j] = True
    flag = True
    while que and flag:
        v = que.popleft()
        for x,y in d[v]:
            if honest[x] == -1:
                honest[x] = y
                if y:
                    que.append(x)
            elif honest[x] != y:
                flag = False
                break
    if flag:
        maxi = max(maxi,str(bin(i)).count('1'))
print(maxi)