N = int(input())
A = input()

if len(A) <= N:
  print(A)
else:
  print(A[:N] + '...')