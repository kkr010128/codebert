for m, f, r in ((int(j) for j in i.split()) for i in iter(input, "-1 -1 -1")):
  if m == -1 or f == -1:
    print ('F')
  elif m + f >= 80:
    print ('A')
  elif m + f >= 65:
    print ('B')
  elif m + f >= 50 or (m + f >= 30 and r >= 50):
    print ('C')
  elif m + f >= 30:
    print ('D')
  else:
    print ('F')