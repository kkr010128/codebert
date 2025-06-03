import sys
n=int(input())
l=n//100
d=n%100
for i in range(5, 0, -1):
  if d // i > 0:
    l = l - (d // i)
    d = d - i * (d // i)
  if d == 0 and l >= 0:
    print(1)
    sys.exit()
  if l < 0:
    break
print(0)