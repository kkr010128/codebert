array = []
for i in range(3,int(input()) + 1):
  if i % 3 == 0 or i % 10 == 3 or '3' in str(i):
    array.append(i)
for i in array:
  print('',"{0}".format(i),end='')
print()