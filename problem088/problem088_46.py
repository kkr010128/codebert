n=int(input())
alist=list(map(int,input().split()))
height=alist[0]
ans=0

for i in range(1,n):
    if height>alist[i]:
        ans+=height-alist[i]
    
    else:
        height=alist[i]

print(ans)