#! python3

a, b = [int(x) for x in input().strip().split(' ')]
if a > b:
  print('a > b')
elif a < b:
  print('a < b')
else:
  print('a == b')