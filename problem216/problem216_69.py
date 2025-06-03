a,b,c = input().split()
if a==b and b==c:
  print('No')
elif a==b or b==c or c==a:
  print('Yes')
else:
  print('No')