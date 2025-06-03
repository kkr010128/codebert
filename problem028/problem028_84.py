n,m=map(int,input().split())
x=list(map(int,input().split()))

memo=[n+1 for _ in range(n+1)]
memo[n]=0

for i in range(n,-1,-1):
    for xx in x:
        if i-xx<0:
            continue
        memo[i-xx]=min(memo[i-xx],memo[i]+1)
print(memo[0])
