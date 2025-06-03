x = int(input())
for a in range(x):
 y = map(int,raw_input().split())
 y.sort()
 if y[2]**2-y[1]**2 == y[0]**2:
  print "YES"
 else:
  print "NO"