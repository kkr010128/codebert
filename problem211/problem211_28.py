a, b = list(map(int, input().split()))
if a >= 10:
  my_result = b
else:
  my_result = b + 100 * (10 - a)
print(my_result)