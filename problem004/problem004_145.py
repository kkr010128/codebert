n = int(input())
for i in range(n):
  l = [int(j) for j in input().split()]
  l.sort()
  print("YES" if l[0]**2 + l[1]**2 == l[2]**2 else "NO")