n=int(input())
A=sorted(list(map(int,input().split())))
ans=0
if n==1 : print(0);exit()
for i in range(n-1):
    # if i==0 : ans+=A[-1];continue
    ans+=A[-((i+1)//2+1)]

print(ans)