nd = list(map(int, input().split()))
N = nd[0]
D = nd[1]
ans = 0
for i in range(N):
  x = list(map(int, input().split()))
  if x[0] ** 2 + x[1] ** 2 <= D ** 2:
    ans += 1
print(ans)
