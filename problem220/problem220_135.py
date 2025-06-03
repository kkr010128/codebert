l = list(input() for _ in range(3))
str1 , str2 = l[0].split()
num1 , num2 = map(int,l[1].split())
if l[2] == str1:
  num1 -= 1
  print(num1 , num2)
else:
  num2 -= 1
  print(num1 , num2)