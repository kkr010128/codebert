n = int(input())
x = n%10
a = [0,1,6,8]

if x == 3:
  print('bon')
elif x in a:
  print('pon')
else:
  print('hon')