S,T=map(str,input().split())
A,B=map(int,input().split())
U=str(input())

if S==U:
  print(str(A-1)+" "+str(B))
else:
  print(str(A)+" "+str(B-1))
