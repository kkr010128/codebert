n = int(input())
a = list(map(int, input().split()))
ans = 10**9
for i in range(0, 101):
  temp = 0
  for x in a:
    temp += (x-i)**2
  ans = min(ans, temp)
print(ans)
