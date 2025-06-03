while 1:
  m, f, r = map(int, input().split())
  s = m + f
  if m == -1 and f == -1 and r == -1:
    break
  elif m == -1 or f == -1 or s < 30:
    print("F")
  elif s >= 80:
    print("A")
  elif s >= 65 and s < 80:
    print("B")
  elif s >= 50 and s < 65:
    print("C")
  elif s >= 30 and s < 50:
    if r < 50:
      print("D")
    else:
      print("C")
