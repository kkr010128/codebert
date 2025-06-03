x = int(input())

a = 0
b = 0
flg = True

while True:
  a += 1
  for i in range(a):
    if a**5 - i**5 == x:
      a = a
      b = i
      flg = False
      break
    elif a**5 + i**5 == x:
      a = a
      b = -i
      flg = False
      break
  if flg == False:
    break
  
a = str(a)
b = str(b)
print(a+' '+b)