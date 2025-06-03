N = input()
A, a = 0, 0
for i in range(65, 91):
  if i==ord(N):
    A += 1
for i in range(97, 123):
  if i==ord(N):
    a += 1
if A==1:
  print('A')
if a==1:
  print('a')