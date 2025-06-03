i = list(map(int, input().split()))
ans=0
for j in range(i[0],i[1]+1):
    if j%i[2] ==0:
        ans+=1
print(ans)
