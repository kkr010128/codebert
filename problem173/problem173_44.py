sm=0
for i in range(1,int(input())+1):
  if (i%3)*(i%5)>0:
    sm+=i
print(sm)