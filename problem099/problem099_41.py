n,k=map(int,input().split())
A=list(map(int,input().split()))

ng=0
ok=max(A)


while abs(ok-ng)>1:
    mid=(ok+ng)//2
    
    now=0
    for i in A:
        now+= i//mid-1 if i%mid==0 else i//mid
    if now> k :
        ng=mid
    else:
        ok=mid

print(ok)