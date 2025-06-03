a = [int(input()) for i in range(2)]
if a[0] == 1:
  if a[1] == 2:
    my_result = 3
  else:
    my_result = 2
elif a[0] == 2:
  if a[1] == 1:
    my_result = 3
  else:
    my_result = 1
else:
  if a[1] == 1:
    my_result = 2
  else:
    my_result = 1
print(my_result)