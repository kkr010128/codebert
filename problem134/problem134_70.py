n=int(input())
array=list(map(int,input().split()))
ans=1
if 0 in array:
  ans=0
else:
  for i in range(n):
    if ans>10**18:
      break
    else:
      ans=ans*array[i]
if ans>10**18:
  print(-1)
else:
  print(ans)