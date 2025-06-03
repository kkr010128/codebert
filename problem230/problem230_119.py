ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,d,a = mi()
lis = []
for  i in range(n):
    x,h = mi()
    h = (h + a - 1) // a
    lis.append([x,h])

lis.sort()
dis = []
hp = []
for i in range(n):
    dis.append(lis[i][0])
    hp.append(lis[i][1])
#imos?
from collections import deque
hiku = deque()
sums = hp[0]
ans = hp[0]
hiku.append([dis[0] + 2 * d,hp[0]])
imadis,imahp = hiku.popleft()
for i in range(1,n):
    while True:
        if dis[i] <= imadis:
            break
        else:
            sums -= imahp
            imahp = 0
            if hiku:
                imadis,imahp = hiku.popleft()
            else:
                break
    diff = hp[i] - sums
    if diff > 0:
        ans += diff
        sums += diff
        hiku.append([dis[i] + 2 * d,diff])

print(ans)
