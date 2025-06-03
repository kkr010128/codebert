n,m = map(int,input().split())
c1 = []
c2 = []
c3 = []
for i in range(m):
  sc = list(map(int,input().split()))
  if sc[0] == 1:
    c1.append(sc[1])
  elif sc[0] == 2:
    c2.append(sc[1])
  else:
    c3.append(sc[1])

if len(set(c1)) <= 1 and len(set(c2)) <= 1 and len(set(c3)) <= 1:
  if 0 in list(set(c1)):
    if n == 1 and len(set(c1)) == 1 and len(set(c2)) == 0 and len(set(c3)) == 0:
      print('0')
      exit()
    else:
      print('-1')
      exit()
  elif not c1 and not c2 and not c3:
    if n == 1:
      print('0')
      exit()
    elif n == 2:
      print('10')
      exit()
    else:
      print('100')
      exit()
  else:
    if list(set(c1)):
      ans_c1 = list(set(c1))[0]
    else:
      ans_c1 = 1
    if list(set(c2)):
      ans_c2 = list(set(c2))[0]
    else:
      ans_c2 = 0
    if list(set(c3)):
      ans_c3 = list(set(c3))[0]
    else:
      ans_c3 = 0
else:
  print('-1')
  exit()

if n == 1:
  print(ans_c1)
elif n == 2:
  print(ans_c1*10 + ans_c2)
else:
  print(ans_c1*100 + ans_c2*10 + ans_c3)