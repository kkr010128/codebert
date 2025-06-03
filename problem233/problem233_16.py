input()
P=map(int,input().split())
ans,mn=0,2*10**5
for x in P:
    if mn>=x: ans+=1; mn=x
print(ans)
