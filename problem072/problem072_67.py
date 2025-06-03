N=int(input())
ans=0
ke=0
for i in range(N):
    D,E=map(int,input().split())
    if D==E:
        ans+=1
    else:
        ans=0
    if ans>=3:
        ke=1
if ke==1:
    print("Yes")
else:
    print("No")