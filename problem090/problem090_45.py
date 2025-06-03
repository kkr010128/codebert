s = str(input())

cnt = s.count("R")

if cnt == 0:
  print(0)
elif cnt == 1:
  print(1)
elif cnt == 2:
  if s[1] == "S":
    print(1)
  else:
    print(2)
elif cnt == 3:
  print(3)