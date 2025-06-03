x,y = map(int, input().split())
ans = 'false'

for i in range(0,x+1):
  if y == 2*i + 4*(x-i):
    ans = 'true'
    break

if ans == 'true':
  print('Yes')
else:
  print('No')