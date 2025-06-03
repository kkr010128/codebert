n=int(input())
if n%2!=0:
  print(0)
else:
  ans=0
  t=10
  while True:
    ans=ans+n//t
    t=t*5
    if n//t==0:
      break
  print(ans)