N=int(input())
if N==1:
  print('{:.10f}'.format(1))
elif N%2==0:
  print('{:.10f}'.format(0.5))
else:
  print('{:.10f}'.format((N+1)/(2*N)))