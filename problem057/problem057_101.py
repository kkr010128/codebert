while True:
  m,f,r=map(int,input().split())
  if (m,f,r)==(-1,-1,-1):
    break
  h=m+f
  if m == -1 or f == -1:
    print('F')
  elif h >= 80:
    print('A')
  elif h>=65 and h<80:
    print('B')
  elif h>=50 and h<65:
    print('C')
  elif h>=30 and h<50 and r>=50:
    print('C')
  elif h>=30 and h<50 and r<50:
    print('D')
  else:
    print('F')
