n,m=map(int,input().split())
num=[-1]*(n)
total=""
ans=-1
if n==1 and m==0:
    print(0)
    exit()
for i in range(m):
    a,c=map(int,input().split())
    if num[a-1]==-1 or num[a-1]==c:
        num[a-1]=c
    elif num[a-1]!=-1 and num[a-1]!=c:
        print(ans)
        exit()
for i in range(n):
    if num[i]==-1:
        if i==0:
            num[i]=1
        else:
            num[i]=0
for i in range(n):
    total+=str(num[i])
total=int(total)
total=str(total)
if len(total)==n:
    ans=int(total)
print(ans)