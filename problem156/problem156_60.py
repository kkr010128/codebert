num=(int)(input())
for i in range(-64, 121):
  for j in range(-64, 121):
    if i**5-j**5== num:
      print(i, j)
      break
  else:
    continue
  break