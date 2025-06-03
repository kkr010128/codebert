n = int(input())
x = [int(y.strip()) for y in input().split()]
lower = min(x)
upper = max(x)
i = lower
ans = 10000*100
for i in range(upper+1):
  ttl = 0
  for j in x:
    dist = (j - i)**2
    ttl = ttl + dist
  if ttl < ans:
    ans = ttl
print(ans)