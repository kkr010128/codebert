X = int(input())
if X == 2:
  print(2)
  exit()

count = 0
if X % 2 == 0:
  X += 1
while True:
  now = X + count
  k = 3
  while k*k <= now:
    if now % k == 0:
      count += 2
      break
    else:
      k += 2
      continue
  if k*k > now:
    break
  
  
print(now)