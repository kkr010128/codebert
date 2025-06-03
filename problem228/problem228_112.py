h = int(input())
ans = 0
i = 0
while True:
  if(2**i>=h):
    break
  i+=1
if(i == 0):
  print(1)
elif(2**i==h):
  print(2**(i+1)-1)
else:
  print(2**i-1)
