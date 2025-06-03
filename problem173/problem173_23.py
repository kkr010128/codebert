N = int(input())
ans = 0
for i in range(N):
  n = i + 1
  if n % 3 == 0 or n % 5 == 0:
    continue
  else:
    ans += n
print(ans)