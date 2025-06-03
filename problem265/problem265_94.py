import math

n=int(input())

num=math.ceil(n/1.08)

if math.floor(num*1.08)==n:
  print(num)
else:
  print(":(")
