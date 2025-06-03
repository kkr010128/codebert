N=int(input())
c=[[0 for _ in range(10)] for _ in range(10)]
for h in range(1,N+1):
    num=str(h)
    c[int(num[-1])][int(num[0])]+=1

ans=0
for i in range(10):
    for j in range(10):
        ans+=c[i][j]*c[j][i]

print(ans)