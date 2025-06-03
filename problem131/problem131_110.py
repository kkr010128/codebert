A,V=map(int,input().split()) #A：鬼
B,W=map(int,input().split()) #B:逃走者
T=int(input())

dis=abs(A-B)
time=V-W #逃走者から見た鬼の秒速(鬼の方が早いとtime>0、それ以外の場合はtime<=0)

if time<=0:
  print('NO')
else:
  if time*T>=dis:
    print('YES')
  else:
    print('NO')
