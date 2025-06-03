S=int(input())
ans=[0]*(S+1)
MOD=10**9+7

if S<=2:
    print(0)
    exit(0)
elif S==3:
    print(1)
    exit(0)   
ans[3]=1
for i in range(4,S+1):
    ans[i]=ans[i-1]+ans[i-3]

print(ans[i]%MOD)