N = int(input())
ans = 0
for i in range(N):
  j = i + 1
  if j % 3 != 0 and j % 5 != 0:
    ans += j
print(ans)