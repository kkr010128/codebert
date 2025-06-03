N=int(input())
ai=list(map(int,input().split()))

ans=0

for i in range(N):
    if i%2==1:
        continue

    if ai[i] %2==1:
        ans+=1
print(ans)
