K=int(input())

if K<=9:
  print(K)
else:
  p=1
  dp,old=[[1]*10],[0,1]
  n=9
  while K>n:
    old=dp[p-1]
    tmp=[0]*10
    for i in range(1,9):
      tmp[i]=old[i-1]+old[i]+old[i+1]
    tmp[9]=old[8]+old[9]
    tmp[0]=old[0]+old[1]
    dp.append(tmp)
    p+=1
    n+=sum(tmp[1:])

  ans=0
  n-=sum(tmp[1:])
  K-=n
  c=2
  for i in range(p-1,-1,-1):
    if c!=0:
      c-=1
    while K>dp[i][c]:
      K-=dp[i][c]
      c+=1
    ans+=c*10**i
  print(ans)