H = int(input())
W = int(input())
N = int(input())

X = 0

if H <= W:
  X = N // W
  if N % W != 0:
    X = X + 1
else :
  X = N // H
  if N % H != 0:
    X = X + 1
  
print(X)