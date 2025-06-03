import math

S = list(map(int, input().split()))
a = (S[2]-S[0])*60+(S[3]-S[1])
b = a - S[4]
if(b>0):
  print(b)
else:
  print(0)