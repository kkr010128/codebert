N = input()
list = []
for i in range(len(N)):
  list.append(int(N[i]))
  
if sum(list) % 9 ==0:
  print('Yes')
else:
  print('No')


