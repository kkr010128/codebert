s = input()
summation = sum([int(i) for i in s])
is_mul = summation%9
if is_mul == 0:
  print("Yes")
else:
  print("No")