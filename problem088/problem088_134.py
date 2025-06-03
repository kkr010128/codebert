n = int(input())
num = list(map(int,input().split()))
ans = 0
m = num[0]

for i in range(1,n):
  if m >= num[i]:
    ans += m - num[i]
  else:
    m = num[i]
print(ans)