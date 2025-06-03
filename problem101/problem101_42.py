tmp = input().split()
map_tmp = map(int, tmp)
values = list(map_tmp)
moves = int(input())

while(moves):
  if (values[1] <= values[0]):
  	values[1] *= 2
  	moves -=1
  elif(values[2] <= values[1]):
    values[2] *=2
    moves -=1
  else:
    break
    
if (values[1] > values[0]) and (values[2] > values[1]):
  print('Yes')
else:
  print('No')
