X, N = map(int, input().split())
if not N == 0:
  p_l = list(map(int, input().split()))
if N == 0:
  print(X)
  exit()
a = b = X
if not a in p_l:
  if not b in p_l:
    if a > b:
      print(b)
      exit()
    else:
      print(a)
      exit()
  print(a)
  exit()
elif not b in p_l:
  if not a in p_l:
    if a > b:
      print(b)
      exit()
    else:
      print(a)
      exit()
  print(b)
while True:
  a += 1
  if b > 0:
    b -= 1
  if a in p_l and b in p_l:
    continue
  if not a in p_l:
    if not b in p_l:
      if a > b:
        print(b)
#        print("A")
        exit()
      else:
#        print("B")
        print(a)
        exit()
#    print("C")
    print(a)
    exit()
  elif not b in p_l:
    if not a in p_l:
      if a > b:
        print(b)
#        print("D")
        exit()
      else:
        print(a)
#        print("E")
        exit()
#    print("F")
    print(b)
    exit()