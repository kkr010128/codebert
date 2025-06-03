N=int(input())
A=list(map(int,input().split()))
ans=0
tree=1
node=sum(A)
flag=0
for i in A:
    ans+=i
    node-=i
    if i>tree:
        ans=-1
        break
    tree-=i
    if tree<node:
        ans+=tree
    else:
        ans+=node
    tree=2*tree
print(ans)