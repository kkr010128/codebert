k = int(input())
a, b = map(int, input().split())
f = False

for i in range(a, b+1):
  if i%k == 0:
    print('OK')
    f = True
    break

if f is False:
  print('NG')  
