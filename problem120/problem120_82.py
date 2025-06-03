n,k=input().split()
n=int(n)
k=int(k)
clist=list(map(int,input().split()))
clist.sort()

print(sum(clist[:k]))