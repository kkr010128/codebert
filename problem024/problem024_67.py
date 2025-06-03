n,k=map(int,input().split())
tmp=[int(input()) for i in range(n)]
 
left=max(tmp)-1
right=sum(tmp)
while left+1 < right:
    mid=(left+right)//2
    count=1
    now=0
    for i in tmp:
        if mid<now+i:
            now=i
            count+=1
        else:
            now+=i
 
    if count<=k:
        right=mid
    else:
        left=mid
print(right)
