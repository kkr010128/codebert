a = int(input())
b = a % 2
if b == 0:
  my_result = 0.5
else:
  my_result = (a + 1) / (2 * a)
print(my_result)