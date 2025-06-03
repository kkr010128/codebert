x=int(input())

for i in range(x,10**6+1):
  now=i-1
  flag=0
  while(2<=now):
    if i%now==0:
      flag=1
      break
    now-=1
  if flag==0:
    print(i)
    break
