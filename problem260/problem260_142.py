s=input()
values=[int(val) for val in s.split()]
if sum(values)>=22:
  print("bust")
else:
  print("win")