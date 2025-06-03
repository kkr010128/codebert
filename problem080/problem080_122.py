N=int(input())
x=[0]*N
for i in range(N):
    x[i]=list(map(int,input().split()))
#print(x)
z=[0]*N
w=[0]*N

for i in range(N):
    z[i]=x[i][0]+x[i][1]
    w[i]=x[i][0]-x[i][1]

print(max(max(z)-min(z),max(w)-min(w)))
