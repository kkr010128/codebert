a, b, c = list(map(int, input().split()))
if a==b or b==c or c==a:
  if a==b==c:
    my_result = 'No'
  else: 
    my_result = 'Yes'
else:
  my_result = 'No'
print(my_result)