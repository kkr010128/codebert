#keyence c subarry sum
n,k,s=map(int,input().split())
x=10**9
ans=[print(s) for _ in range(k)]
for i in range(n-k):
    if s==x:
        print(1)
    else:
        print(s+1)