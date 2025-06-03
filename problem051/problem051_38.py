H = []
W = []
i = 0
while True:
  h, w = map(int, input().split())
  H.append(h)
  W.append(w)
  if H[i] == 0 and W[i] == 0:
    break
  i += 1

i = 0
while True:
  if H[i] == 0 and W[i] == 0:
    break
  for j in range(H[i]):
    if j % 2 == 1:
      for k in range(W[i]):
        if k % 2 == 1:
          print("#", end = "")
        elif k % 2 == 0:
          print(".", end = "")
    elif j % 2 == 0:
      for k in range(W[i]):
        if k % 2 == 1:
            print(".", end = "")
        elif k % 2 == 0:
            print("#", end = "")
    print()
  print()
  i += 1