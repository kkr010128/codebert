X = int(input())
A = 0
f = 1
while f:
  a = A ** 5
  B = 0
  while f:
    b = B ** 5
    if a <= X:
      if a + b == X:
        print(str(A)+" "+str(-B))
        f = 0
      elif a + b > X:
        break
    if a > X:
      if a - b == X:
        print(str(A)+" "+str(B))
        f = 0
      elif a - b < X:
        break
    B += 1
  A += 1