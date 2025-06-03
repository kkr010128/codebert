x = int(input())
ans = x
while True:
  jud = 0
  if(ans <= 2):
    print(2)
    break
  if(ans%2==0):
    jud += 1
  i = 3
  while i < ans**(1/2):
    if(jud>0):
      break
    if(ans%i == 0):
      jud += 1
    i += 2
  if(jud==0):
    print(ans)
    break
  ans += 1
 