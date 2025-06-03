n=int(input())
a=list(map(int,input().split()))
p=[]
m=[]
for i in range(n):
    p.append(i+a[i])
    m.append(i-a[i])
x=[0]*(2*n)
y=[0]*(2*n)
ans=0
for i in range(n):
    if 0<=p[i]<=(2*n)-1:
        x[p[i]]+=1
    if 0<=m[i]<=(2*n)-1:
        y[m[i]]+=1
for i in range(n):
    ans+=x[i]*y[i]
print(ans)