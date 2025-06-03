n = input()
if len(n) < 3:
  print(1000 - int(n))
else:
  hasuu = n[len(n) - 3:]
  if hasuu == '000':
    print('0')
  else:
    print(1000-int(hasuu))