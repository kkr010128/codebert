def yes(N,M):
  N+=1
  print('YNeos'[M::N])
  return

a,b=map(int,input().split())
if 500*a >= b:
  yes(1,0)
else:
  yes(1,1)