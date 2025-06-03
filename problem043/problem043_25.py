c = 0

while True:
  a,b = map(int, input().split()); c+=1
  if a < b:
    print(a,b)
  elif a >b:
    print(b,a)
  elif a ==b and a !=0 and b!=0:
    print(a,b)
 
  elif a ==0 and b == 0: break
  
