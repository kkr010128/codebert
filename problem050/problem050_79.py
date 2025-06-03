for i in range(10000):
  x = input().split()
  h = int(x[0])
  w = int(x[1])
  if h == 0 and w ==0:
    break
  for i in range(w):
    print("#",end="")
  print()  
  for i in range(h-2):
    print("#",end="")
    for i in range(w-2):
      print(".",end="")
    print("#",end="")
    print()
  for i in range(w):
    print("#",end="")
  print()
  print()  
