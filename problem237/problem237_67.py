n = int(input())
l = [[] for _ in range(n)]
d = [[] for _ in range(n)]
for i in range(n):
    l[i] = list(map(int,input().split()))
    d[i] = [l[i][0]-l[i][1],l[i][0]+l[i][1]]

d.sort(key=lambda x:x[1])
ma = -9999999
c = 0
for i in range(n):
    if(d[i][0] >= ma):
        ma = d[i][1]
        c += 1
print(c)