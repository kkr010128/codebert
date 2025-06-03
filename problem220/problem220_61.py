S, T = input().split()
A, B = (int(x) for x in input().split())
U = input()
if S == U or T == U:
  print(A - int(S==U), B - int(T==U))
  
