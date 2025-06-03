a, b, c, d = list(map(int, input().split()))
turn = True
while True:
  if turn:
    c -= b
    if c <= 0:
      print("Yes")
      import sys
      sys.exit()
  else:
    a -= d
    if a <= 0:
      print("No")
      import sys
      sys.exit()
  turn ^= True
