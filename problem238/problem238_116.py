#C
n,k,s = map(int,input().split())

ans = [1 for _ in range(n)]

for i in range(k):
    ans[i] = s

for j in range(n-k):
    if s != 1:
        ans[k+j] = s//2 + 1
    else:
        ans[k+j] = s//2 + 2
print(*ans)