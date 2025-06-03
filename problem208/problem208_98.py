n,m = map(int,input().split())

A=[-1]*n

ans=0
for i in range(m):
    s,c = map(int,input().split())
    if A[s-1]!=-1 and A[s-1]!=c :
        ans=-1
        break
    else:
        A[s-1]=c

if A[0]==0 and n!=1 :
    ans=-1

if ans==-1 :
    print(ans)
    exit()
    
if A[0]==-1 and n!=1 :
    A[0]=1
for i in range(n):
    ans*=10
    if A[i]==-1 :
        A[i] = 0
    ans += A[i]



print(ans)