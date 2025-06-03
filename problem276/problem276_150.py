A=int(input())
l=list(map(int,input().split()))
right=l[0]
left=sum(l[1:])
ans=left-right
for i in range(A-2):
    right+=l[i+1]
    left-=l[i+1]
    ans=min(ans,abs(right-left))
print(ans)