S, T = input().split()
A, B = map(int, input().split())
U = input()
 
if S == U :
  print(str(A - 1) + ' ' + str(B))
elif T == U :
  print(str(A) + ' ' + str(B - 1))