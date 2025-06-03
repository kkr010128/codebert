n, k = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0
for i in range(n):
  if (lst[i] >= k):
    ans = ans + 1
print(ans)