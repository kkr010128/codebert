a, b, m = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
li_c = []
for _ in range(m):
  x, y, c = map(int, input().split())
  x, y = x-1, y-1
  li_c.append(li_a[x]+li_b[y]-c)
li_a.sort()
li_b.sort()
li_c.sort()
ans = min(li_a[0]+li_b[0], li_c[0])
print(ans)
