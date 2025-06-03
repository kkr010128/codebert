a, b, m = map(int, input().split())
reizo = list(map(int, input().split()))
renji = list(map(int, input().split()))
p = [list(map(int,input().split())) for i in range(m)]
ans = []
for i in range(m):
  cost = reizo[p[i][0] - 1] + renji[p[i][1] - 1] - p[i][2]
  ans.append(cost)
ans.append(min(reizo) + min(renji))
print(min(ans))