import sys
n = input()
for i in range(1,n+1):
  x = i
  if x%3==0:
    sys.stdout.write(' %d' % i)
    continue
  while x<=n:
    if x%10==3:
      sys.stdout.write(' %d' % i)
      break
    else:
      x /= 10
      if x==0:
        break
sys.stdout.write('\n')