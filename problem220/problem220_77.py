S,T,A,B,U = open(0).read().split()

if S==U:
  print(int(A)-1,B)
else:
  print(A,int(B)-1)