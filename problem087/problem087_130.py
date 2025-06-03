target = input()
sum = 0
for each in target:
  sum += int(each)
if sum % 9 == 0:
  print("Yes")
else:
  print("No")