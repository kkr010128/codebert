N = int(input())
P = list(map(int, input().split()))

mini = N + 1
ans = 0
for i in range(N):
  if P[i] < mini:
    ans += 1
    mini = P[i]

print(ans) 