N,K=list(map(int,input().split()))

ans_=[0]*N

for k in range(0,2*K,2):
    k_ = int(input())
    A = list(map(int,input().split()))
    for a in A:
        ans_[a-1]+=1
        
ans=0
for a in ans_:
    if a == 0:
        ans+=1
        
print(ans)