n = int(input())
a = [[0, 0] for i in range(n)]
for i in range(n):
  x, l = list(map(int, input().split()))
  a[i] = [x + l, max(x - l, 0)]
a.sort()
ans = 0
p = 0
for i in a:
  if p <= i[1]:
    ans += 1
    p = i[0]
print(ans)