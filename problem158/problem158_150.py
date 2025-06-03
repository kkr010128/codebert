n = int(input())
a,b = map(int, input().split())
F = True

while a<=b:
  if a%n == 0:
    print('OK')
    F = False
    break 
  a += 1

if F:
  print('NG')