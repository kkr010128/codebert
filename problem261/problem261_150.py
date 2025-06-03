lit = input()
length = len(lit)
times = 0
if length != 1:
  for i in range(int(length/2)):
     if lit[i] != lit[length-1-i]:
       times += 1
  print(times)
else:
  print(times)