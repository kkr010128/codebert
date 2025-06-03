N = int(input())
P = list(map(int, input().split()))

ans = [0]*N
min_cal = [0]*N
min_cal[0] = P[0]

for i in range(N-1):
  min_cal[i+1] = min(min_cal[i],P[i+1])

for i in range(N):
  if min_cal[i] >= P[i]:
    ans[i] = 1

print(sum(ans))