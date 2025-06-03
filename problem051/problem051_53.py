import sys
while 1:
  H, W = map(int, raw_input().split())
  if H==0 and W==0:
    break
  for i in range(H):
    for j in range(W):
      if (i+j)%2==0:
        sys.stdout.write('#')
      else:
        sys.stdout.write('.')
    sys.stdout.write('\n')
  print ''