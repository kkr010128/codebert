count = int(input())
for i in range(count):
  a = map(int,raw_input().split())
  a.sort()
  if a[0]**2+a[1]**2  == a[2]**2: print "YES"
  else: print "NO"