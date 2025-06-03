a, b, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
cost = []
for i in range(m):
  x, y, c = map(int, input().split())
  cost.append(arr_a[x - 1] + arr_b[y - 1] - c)
cost.append(min(arr_a) + min(arr_b))
ans = min(cost)
print(ans)