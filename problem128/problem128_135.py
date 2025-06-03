X, N = map(int, input().split())

if N == 0:
  print(X)
  
else:
  P = list(map(int, input().split()))
  A = [0]
  for i in range(1, 102):
    if (i in P) == False:
      A.append(i)
      
  c = 101
  for j in range(len(A)):
    if abs(X - A[len(A)-int(j)-1]) <= abs(X - c):
      c = A[len(A)-int(j)-1]
    else:
      c = c
  print(c)
  
  
