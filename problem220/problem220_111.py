S, T = input().split()
A, B = input().split()
U = input()
if S==U:
  print(int(A)-1,end=" ")
  print(int(B))
else:
  print(int(A),end=" ")
  print(int(B)-1)