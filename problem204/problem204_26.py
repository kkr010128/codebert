s = input()
sgn = 1
Q = int(input())
L = '' #sgn=-1
R = '' #sgn=1
for _ in range(Q):
  i = input()
  if i[0] == '1':
    sgn*=-1
  else:
    if i[2] == '1':
      if sgn == 1:
        L += i[4]
      else:
        R += i[4]
    else:
      if sgn == 1:
        R += i[4]
      else:
        L += i[4]

if sgn == -1:
  s = s[::-1]
  R = R[::-1]
  print(R + s +L)
  
else:
  L = L[::-1]
  print(L + s + R)