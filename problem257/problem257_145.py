N=int(input())
A=list(map(int,input().split()))
cur=1
for i in range(N):
    if A[i]==cur:
        cur+=1
if cur==1:
    print(-1)
elif cur>1:
    print(N-(cur-1))
