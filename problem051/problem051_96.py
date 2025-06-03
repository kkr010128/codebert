#!/usr/bin/python

ar = []
while True:
  tmp = [int(i) for i in input().split()]
  if tmp == [0,0]:
    break
  else:
    ar.append(tmp)

for i in range(len(ar)):
  for j in range(ar[i][0]):
    for k in range(ar[i][1]):
      if ( j + k ) % 2 == 0:
        print('#' , end='' if k !=ar[i][1]-1 else '\n' if j != ar[i][0]-1 else '\n\n')
      else:
        print('.' , end='' if k !=ar[i][1]-1 else '\n' if j != ar[i][0]-1 else '\n\n')