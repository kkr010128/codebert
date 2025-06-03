S,T=input().split()
A,B=map(int,input().split())
U=input()
if(U==S):
  print("{}".format(A-1)+" {}".format(B))
else:
  print("{}".format(A)+" {}".format(B-1))