count = input()
#print(len(count))
num = 0
for i in range(len(count)):
  num += int(count[i])
if num % 9 == 0:
  print("Yes")
else:
  print("No")