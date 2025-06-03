X=int(input())
N=X%100
if N%5==0:
  if N//5<=X//100:
    print('1')
  else:
    print('0')
else:
  if N//5+1<=X//100:
    print('1')
  else:
    print('0')