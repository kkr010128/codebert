n = int(input())
for i in range(0,10001,1000):
  if i - n >= 0:
    print(i - n)
    exit()
  else:
    continue