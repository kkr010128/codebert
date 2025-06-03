a = int(input())
n = 1
while True:
  if a*n % 360 == 0:
    break
  else:
    n += 1
print(n)