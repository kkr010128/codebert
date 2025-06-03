#init
N = int(input())
S=[]
for _ in range(N):
  S.append(input())
score=[0]*4
for _ in S:
  if _=='AC':
    score[0]=score[0]+1
  if _=='WA':
    score[1]=score[1]+1
  if _=='TLE':
    score[2]=score[2]+1
  if _=='RE':
    score[3]=score[3]+1
    
print('AC x {0}'.format(score[0]))
print('WA x {0}'.format(score[1]))
print('TLE x {0}'.format(score[2]))
print('RE x {0}'.format(score[3]))