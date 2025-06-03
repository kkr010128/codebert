N = int(input())
P = list(map(int,input().split()))

num = float("inf")
ans = 0

for i in range(N):
  if num >= P[i]:
    ans += 1
    num = P[i]
    
print(ans)