# i>j とする.
# |i-j|=Ai+Aj
#  i-j = Ai+Aj

N=int(input())
A=list(map(int,input().split()))
cnt=[0]*300000
ans=0
for i in range(N):
    if i-A[i]>=0:
        ans=ans+cnt[i-A[i]]
    if i+A[i]<len(cnt):
        cnt[i+A[i]]=cnt[i+A[i]]+1
print(ans)
