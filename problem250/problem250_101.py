x = int(input())
if x == 2:
  print(2)
  exit()
  
for i in range(1000000):  
  for j in range(2, x+i):
    
    if (x+i) % j == 0:
      break   
         
    if j == x+i-1:
      print(x+i)
      exit()