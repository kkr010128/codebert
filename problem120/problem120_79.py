N,K=map(int,input().split())
pi=list(map(int,input().split()))
pi_sort=sorted(pi,reverse=False)
ans=0
for i in range(K):
    ans+=pi_sort[i]
print(ans)