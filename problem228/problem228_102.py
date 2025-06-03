H = int(input())
cnt = 0
ans = 0

while(H > 0):
  H = int(H / 2)
  cnt += 1

for i in range(cnt):
  ans += 2 ** i

print(ans)