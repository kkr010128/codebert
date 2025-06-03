x = int(input())
a = 1
flag = True
while flag:
  upper = a**5-x
  b = a
  while True:
    if b**5 == upper:
      flag = False
      a -= 1
      break
    if b**5<upper:
      break
    b -= 1
  a += 1
print(a,b)