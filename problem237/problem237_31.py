n = int(input())
lst = []
for i in range(n):
  x, l = map(int, input().split())
  left = x - l
  right = x + l
  lst.append([left, right])

lst = sorted(lst, key=lambda x: x[1])

ans = 1
limit = lst[0][1]
for i in range(n):
  if lst[i][0] >= limit:
    ans += 1
    limit = lst[i][1]

print(ans)