h,n=list(map(int ,input().split()))
l=list(map(int ,input().split()))
ans=0
count=0
for i in range(0,n):
    ans+=l[i]
    if(ans==h or ans>h):
        count+=1
    else:
        count+=0
        
        
        
if(count>0):
    print("Yes")
else:
    print("No")