num=(int)(input())
n=num//100
amari=num%100
if num <= 99 or amari / n > 5:
  print(0)
else:
  print(1)