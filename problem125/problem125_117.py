x = int(input())
k = 1
while(True):
  if k * x % 360 == 0:
    print(k)
    break
  else:
    k += 1