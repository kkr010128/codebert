N = int(input())
X = list(map(int,input().split()))
ans = float("inf")
for loc in range(-100,101):
  temp = 0
  for x in X:
    temp += (loc-x)**2
  ans = min(temp,ans)
print(ans)