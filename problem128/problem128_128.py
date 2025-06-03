inp = [int(a) for a in input().split()]
X = inp[0]
N = inp[1]
if N == 0:
  print(X)
else:
  P = [int(b) for b in input().split()]

  found = 0
  num = 0
  answer = X
  while(found == 0):
    if not (X - num in P):
      found = 1
      answer = X - num
    elif not (X + num in P):
      found = 1
      answer = X + num
    num += 1
  print(answer)