N,D=map(int,input().split())
ans=0
for _ in range(N):
    X,Y=map(int,input().split())
    if X*X+Y*Y<=D*D:
        ans+=1
print(ans)
