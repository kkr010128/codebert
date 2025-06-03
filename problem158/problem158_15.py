k = int(input())
a, b = map(int, input().split())
x = 0
  
while True:
  x += k
  
  if a <= x <= b:
    print('OK')
    break
  
  if x > b:
    print('NG')
    break