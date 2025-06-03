X = int(input())-1

if X==1:
  print(X+1)
  
else:
  while True:
    X+=1
    R = int(X/2)+1 if X>5 else X
    for i in range(2, R):
      if X % i == 0:
        break

    if i==R-1:
      break

  print(X)