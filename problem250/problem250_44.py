x = int(input())
 
while True:
  flag =0
  for i in range(2,x//2):
    if x%i==0:
      flag =1
      break
  if flag ==0:
    print(x)
    exit()
  x = x+1