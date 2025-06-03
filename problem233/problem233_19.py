N = int(input())
P = [int(x) for x in input().split()]
ans = 1
min_p = P[0]
for i in range(1,N):
  if(min_p >= P[i]):
    ans += 1
    min_p = P[i]
print(ans)