N = int(input())
A = [int(x) for x in input().split()]
B = list(set(A))
if(len(A)==len(B)):
  print('YES')
else:
  print('NO')