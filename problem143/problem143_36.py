x=int(input())
y=str(input())
if len(y) > x:
  print(y[:x] + '...')
else:
  print(y)