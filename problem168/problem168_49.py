a, n = input().split()
a = int(a)
n = int(n)
p = list(map(int, input().split()))

c = 0
for i in range(n):
  c += p[i]
  
if c > a:
  print(-1)
else:
  print(a-c)

