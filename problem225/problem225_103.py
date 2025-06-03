a, b = list(map(int, input().split()))
c = a % b
if c == a:
  my_result = 1
elif c == 0:
  my_result = a / b
else:
  my_result = (a - c) / b + 1
print(int(my_result))