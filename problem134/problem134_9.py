n = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst)
ans = 1
for i in range (n):
  ans = ans*lst[i]
  if (ans > 10**18):
    ans = -1
    break
print(ans)
