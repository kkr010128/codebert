import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L=[-1]*n
if n==1 and m==0:
    print(0)
    sys.exit()
for i in range(m):
    s,c=map(int,input().split())
    s-=1
    if L[s]==-1 or L[s]==c:
        L[s] = c
    else:
        print(-1)
        sys.exit()
if L[0]==0 and n>1:
    print(-1)
    sys.exit()
    
for i in range(n):
    if L[i]==-1:
        if i==0:
            L[i]=1
        else:
            L[i]=0
print(*L,sep="")
