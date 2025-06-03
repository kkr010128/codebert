x = int(input())
xSum = 0
cnt = 1
 
while True:
  xSum += x
  if xSum%360 == 0:
    break
  cnt += 1
print(cnt)