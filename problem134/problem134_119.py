n = int(input())
p = list(map(int,input().split()))

ans = 1
dotira = False
s = 10**18

if 0 in p :
  print(0)

else:
  
  for x in p:
    ans = ans * x
    if ans > s:
      dotira = True
      break
  if dotira:
    print(-1)
  else:
    print(ans)

    
