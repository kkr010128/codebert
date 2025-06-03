S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()

a = A - 1
b = B - 1

if U == S:
  print('{} {}'.format(a,B))
else:
  print('{} {}'.format(A,b))
