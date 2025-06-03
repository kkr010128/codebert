X = int(input())
i = 1
while i <= 360:
  if i * X % 360 == 0:
    print(i)
    break
  else:
    i += 1