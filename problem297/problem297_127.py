N=int(input())
if N%2==0:
  print('{:.10f}'.format(0.5))
else:
  print('{:.10f}'.format((N+1)/(2*N)))