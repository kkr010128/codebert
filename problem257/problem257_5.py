n = int(input())
alst = list(map(int, input().split()))
if 1 not in alst:
  print(-1)
  exit()

ans = 0
for num in alst:
    if num == ans + 1:
        ans += 1
else:
    print(n - ans)