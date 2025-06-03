x = input().split()
i = list(map(int,x))
a = i[0]
b = i[1]

if a > b:
  print('a > b')
elif a == b:
  print('a == b')
else:
  print('a < b')