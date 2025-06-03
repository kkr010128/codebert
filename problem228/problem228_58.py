import bisect

H=int(input())
A=[2**x for x in range(51)]

if H==1:
  print(1)
elif H==2:
  print(3)
else:
  index=bisect.bisect_right(A,H) 
  print(sum(A[:index]))