A,B,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
li2=[input() for i in range(m)]
c = []
for i in range(m):
    c.append( [int(x.strip()) for x in li2[i].split()])

ans = min(a) + min (b)

for i in range(m):
    keep = a[c[i][0]-1] + b[c[i][1]-1] - c[i][2]
    if keep < ans:
        ans = keep

print(ans)