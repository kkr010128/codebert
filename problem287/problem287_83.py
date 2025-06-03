import sys
n = int(input())

for i in range(1,10):
  mod,ret = divmod(n,i)
  if ret == 0 and  mod <= 9:
    print('Yes')
    sys.exit()
print('No')