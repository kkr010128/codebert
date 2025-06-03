a, b = list(map(int, input().split()))
if a <= b:
  my_result = 'unsafe'
else:
  my_result = 'safe'
print(my_result)