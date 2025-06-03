h,w=map(int,input().split())
m=[[1 if c=="#" else 0 for c in input()] for i in range(h)]

n=[i[:] for i in m]


for i in range(1,h):
    n[i][0]=n[i-1][0]+int(m[i-1][0]-m[i][0]==-1)
for j in range(1,w):
    n[0][j]=n[0][j-1]+int(m[0][j-1]-m[0][j]==-1)

for i in range(1,h):
    for j in range(1,w):
        n[i][j]=min(n[i-1][j]+int(m[i-1][j]-m[i][j]==-1),n[i][j-1]+int(m[i][j-1]-m[i][j]==-1))

print(n[-1][-1])