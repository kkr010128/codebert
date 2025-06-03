digits = [int(i) for i in list(input())]
Sum = 0
for i in digits:
  Sum += i
if Sum%9 == 0:
  print("Yes")
else:
  print("No")