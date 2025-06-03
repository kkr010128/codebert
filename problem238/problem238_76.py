n,k,s=list(map(int,input().split()))

if s>n:
    ans=["1" for _ in range(n)]
else:
    ans=[str(s+1) for _ in range(n)]

for i in range(k):
    ans[i]=str(s)

print(" ".join(ans))