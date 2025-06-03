N = int(input())
A = list(map(int, input().split()))

m = set(A)
M = len(m)

if N == M:
  print("YES")
  
else:
  print('NO')