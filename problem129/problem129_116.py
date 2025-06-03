N = int(input())
A = list(map(int,input().split()))
m = max(A) + 1
cnt = [0]*m
for i in A:
    cnt[i] += 1
ans = 0
for i in range(1,m):
    if cnt[i]:
        if cnt[i]==1:
            ans += 1
        for j in range(i,m,i):
            cnt[j] = 0
print(ans)