n = int(input())
a = list(map(int,input().split()))
barlen = 0
for x in a:
  barlen += x
halflen = barlen/2
curbarlen = 0
minhalfdis = barlen
for i in range(n):
  curbarlen += a[i]
  minhalfdis = min(minhalfdis,abs(halflen-curbarlen))
print(int(minhalfdis*2))