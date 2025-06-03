a = [int(s) for s in input().split()]
b = int(a[0] // (a[1] + a[2]))
c = int(a[0] % (a[1] + a[2]))
d = b * a[1]
if c >= a[1]:
  d = d + a[1]
else:
  d = d + c

print(d)