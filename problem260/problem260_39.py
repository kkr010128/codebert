A,B,C = map(int,input().split())
ans = A+B+C
if ans <= 21:
  print('win')
else:
  print('bust')