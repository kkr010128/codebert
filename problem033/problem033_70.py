def rot(dice, I):
  #USEWND
  #NEWSUD
  a = dice[:]
  if I=='N': x=[0,4,5,1,0]
  elif I=='E': x=[0,2,5,3,0]
  elif I=='W': x=[0,3,5,2,0]
  elif I=='S': x=[0,1,5,4,0]
  for i in [0,1,2,3]: a[x[i+1]]=dice[x[i]]
  return a

dice = map(int,raw_input().split())
for c in raw_input(): dice = rot(dice,c)
print dice[0]