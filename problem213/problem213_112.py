N = int(input())
X = list(map(int, input().split()))
 
ans = float("inf")
for x in range(max(X)+1):
  ans_temp = 0
  for i in range(N):
    ans_temp += (X[i]-x)**2
  ans = min(ans, ans_temp)
print(ans)