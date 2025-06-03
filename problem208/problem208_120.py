N,M=map(int,input().split())

x=[-1]*N
for _ in range(M):
    s,c=map(int,input().split())
    s-=1
    if (s==c==0 and N>1 or
        x[s]!=-1 and x[s]!=c):
        print(-1)
        exit()
    x[s]=c

if x[0]==-1:
    x[0]=0+(N>1)
for i in range(N):
    if x[i]==-1: x[i]=0

print(''.join(map(str,x)))
