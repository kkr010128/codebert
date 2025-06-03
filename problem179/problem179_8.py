n, m = input().split()
n = int(n)
m = int(m)
c=0

a = list(map(int, input().split()))
for i in range(n):
  c += a[i]
v = c/(4*m)
a.sort(reverse = True)
if a[m-1] < v:
  print('No')
else:
  print('Yes')