import math

N,M=map(int,input().split())

if (N==0 or N==1) and (M==0 or M==1):
  print(0)
elif (N==0 or N==1) and (M!=0 and M!=1):
  print(int(math.factorial(M)/math.factorial(M-2)/math.factorial(2)))
elif (M==0 or M==1) and (N!=0 and N!=1):
  print(int(math.factorial(N)/math.factorial(N-2)/math.factorial(2)))
else:
  print(int(math.factorial(N)/math.factorial(N-2)/math.factorial(2)+math.factorial(M)/math.factorial(M-2)/math.factorial(2)))
