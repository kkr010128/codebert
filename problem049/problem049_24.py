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
    for k in range(W[i]):
      print("#", end="")
    print()
  print()
  i += 1