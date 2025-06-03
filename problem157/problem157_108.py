n=int(input())
a=[0]+list(map(int,input().split()))

cnt={}
ans = 0
for i in range(1,n+1):
    if a[i] +i not in cnt:
        cnt[a[i] +i] = 0
    cnt[a[i] + i] += 1
for i in range(1, n+1):
    if i-a[i] in cnt:
        ans+= cnt[i-a[i]]
print(ans)