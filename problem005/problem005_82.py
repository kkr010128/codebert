while True:
  try:
    m,n = map(int, input().split())
  except EOFError:
    break
  LCM = m * n
  if m < n:
    m,n = n,m

  # calculating GCD
  while True:
    if m % n == 0:
      GCD = n
      break
    else:
      m, n = n, m % n

  # calculating LCM
  LCM = LCM // GCD

  print(GCD,LCM)
