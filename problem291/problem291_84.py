x = list(map(int,input().split()))

a = x[0]
b = x[1]

if(2*b < a):
  print(a-2*b)
else:
  print(0)