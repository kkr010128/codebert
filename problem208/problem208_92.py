import sys
input = sys.stdin.readline
n,m=map(int,input().split())
L=[-1]*n
for i in range(m):
    s,c = map(int,input().split())
    s-=1
    if s>n-1: 
        continue
    if L[s] ==-1 and s<=n-1:
        L[s] = c

    else:
        if L[s]!=c:
            print(-1)
            sys.exit()
    if L[0]==0 and n>1:
        print(-1)
        sys.exit()
if len(L)==1 and L[0]==-1:
    L[0]=0
elif L[0]==-1:
    L[0]=1
for i in range(n):
    if L[i]==-1:
        L[i]=0
print("".join(map(str,L)))
        




