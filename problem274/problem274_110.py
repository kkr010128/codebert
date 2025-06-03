n,m=list(map(int,input().split()))
s=input()
a=[0]*(n+1)
a[0]=1

for i in range(1,n+1):
    if s[i]=='1':
        continue
    for j in range(max(0,i-m),i):
        if s[j]=='1':
            continue
        if a[j]>0:
            break
    
    a[i]=i-j

ans=''

cur=n
while cur>0:
    d=a[cur]
    cur-=d
    if d==0:
        print(-1)
        exit(0)

    ans=str(d)+' '+ans

print(ans[:-1])