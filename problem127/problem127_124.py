a,b = map(int,input().split())
low = a*2
high = a*4
if b%2 != 0:
  print("No")
elif b<low or b>high:
  print("No")
else:
  print("Yes")