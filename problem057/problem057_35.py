while True:
  (m, f, r) = input().rstrip('\r\n').split(' ')
  m = int(m)
  f = int(f)
  r = int(r)
  if m == -1 and f == -1 and r == -1:
    break

  if m == -1 or f == -1:
    print('F')
    continue

  mf = m + f

  if 80 <= mf:
    print('A')
  elif 65 <= mf and mf < 80:
    print('B')
  elif 50 <= mf and mf < 65:
    print('C')
  elif 30 <= mf and mf < 50:
    if 50 <= r:
      print('C')
    else:
      print('D')
  else:
    print('F')

