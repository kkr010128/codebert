n=int(input())
a=list(map(int,input().split()))
M=10**9+7
cnt=[0]*n
ans=1
for i in range(n):
    if a[i]==0:
        cnt[a[i]]+=1
    else:
        ans*=(cnt[a[i]-1]-cnt[a[i]])
        cnt[a[i]]+=1
    ans%=M
for i in range(cnt[0]):
    ans*=3-i
    ans%=M
print(ans)
