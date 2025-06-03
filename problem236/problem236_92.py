A = int (input ())
B = int (input ())
N = int (input ())
if A < B:
  X = N//B
  if N%B == 0:
    print (X)
  else:
    print (X+1)
else:
  X = N//A
  if N%A == 0:
    print (X)
  else:
    print (X+1)