N = int(input())
P = list(map(int, input().split()))
 
mmin = P[0]
ans = 0
for i in range(N):
  if mmin < P[i]:
    continue
  else:
    mmin = P[i]
    ans += 1

print(ans)