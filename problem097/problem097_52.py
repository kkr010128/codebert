k=int(input())
l=[0]*k
x=7%k
s=-1
for c in range(k):
    if x==0:
        s=c+1
        break
    if l[x]==1:
        break
    l[x]=1
    x=(10*x+7)%k
print(s)