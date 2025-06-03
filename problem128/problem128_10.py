x,n=map(int,input().split())
*p,=map(int,input().split())

q=[0]*(102)

for pp in p:
    q[pp]=1
diff=1000
ans=-1

for i in range(0,102):
    if q[i]:
        continue

    cdiff=abs(i-x)

    if cdiff<diff:
        diff=cdiff
        ans=i
    
print(ans)