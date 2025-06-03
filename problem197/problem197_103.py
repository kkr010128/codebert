def readInt():
  return list(map(int, input().split()))
a,b,c = readInt()
judge1 = c-a-b > 0
judge2 = 4*a*b < (c-a-b)**2
if judge1 and judge2:
    print('Yes')
else:
    print('No')