n = int(input())
x = list(map(int, input().split()))
ans = 2000000000
for i in range(1,101):
  sum = 0
  for j in x:
    sum += (i-j)**2
  ans = min(sum, ans)
print(ans)