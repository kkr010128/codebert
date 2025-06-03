x = int(input())
j = 0
for i in range(360):
  j += x
  j %= 360
  if j == 0:
    print(i+1)
    exit()