S, T = input().split()
A, B = map(int, input().split())
U = input()
if (U == T):
  print(str(A)+" "+str(B-1))
else:
  print(str(A-1)+" "+str(B))

