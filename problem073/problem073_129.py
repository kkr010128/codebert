
N=int(input())

ans=0
for a in range(1,N):
    ans+=int((N-1)//a)

print(ans)
