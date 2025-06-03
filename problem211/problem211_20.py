#--Beginner
#1行1列
number, rate = map(int, input().split())

if (number < 10):
  print(rate+(100*(10-number)))
elif (number >= 10):
  print(rate)

