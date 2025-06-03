X = int(input())

wk = 0
cnt = 0
while True:
  wk += X
  cnt += 1
  wk %= 360
  if wk % 360 == 0:
    break
  
print(cnt)