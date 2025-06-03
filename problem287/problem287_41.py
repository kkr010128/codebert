N = int(input())

flag = False
for i in range(1, 10):
  if N//i <= 9 and N%i == 0:
    flag = True
if flag:
  print("Yes")
else:
  print("No")