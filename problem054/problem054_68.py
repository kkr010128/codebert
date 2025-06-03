n = input()
#a,b = map(str,raw_input().split())
a = [raw_input() for i in range(n)]
j=0
for i in range(1,14):
  for j in range(n):
    if a[j] == 'S %s' % i:
      break
    elif j==n-1:
      print 'S %s' % i
for i in range(1,14):
  for j in range(n):
    if a[j] == 'H %s' % i:
      break
    elif j==n-1:
      print 'H %s' % i
for i in range(1,14):
  for j in range(n):
    if a[j] == 'C %s' % i:
      break
    elif j==n-1:
      print 'C %s' % i
for i in range(1,14):
  for j in range(n):
    if a[j] == 'D %s' % i:
      break
    elif j==n-1:
      print 'D %s' % i