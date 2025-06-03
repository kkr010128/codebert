n = int(input())
d = []
z = 0

for i in range(n):
  d1, d2 = map(int, input().split())
  z = z+1 if d1==d2 else 0
  d.append(z)

ans = 'Yes' if max(d)>=3 else 'No'
print(ans)
