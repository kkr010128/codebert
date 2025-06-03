N = str(input())
 
a = []
for n in range(len(N)):
  a.append(int(N[n]))
  
if sum(a) % 9 == 0:
  print('Yes')
else:
  print('No')