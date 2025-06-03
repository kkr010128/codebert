x,n = map(int,input().split())
if n == 0:
  print(x)
  exit()
p = list(map(int,input().split()))

ans = []
num = 0
while ans == []:
  if x + num in p and x - num in p:
    num+=1
  else:
    if x + num not in p and x - num not in p:
      ans = x - num
    elif x + num not in p:
      ans = x + num
    else:
      ans = x - num
print(ans)