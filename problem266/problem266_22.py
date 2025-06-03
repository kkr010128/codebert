X = int(input())

r = X%100

x5 = r//5
r5 = r%5

if r5:
  x5+=1
  
if x5*100 <= X:
  print(1)
else:
  print(0)