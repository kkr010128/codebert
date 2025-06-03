N=int(input())
C=[0]*4
S=['AC','WA','TLE','RE']
for _ in range(N):
  s=input()
  if s==S[0]:
    C[0]+=1
  elif s==S[1]:
    C[1]+=1
  elif s==S[2]:
    C[2]+=1
  else:
    C[3]+=1
for i in range(4):
  print(S[i],'x',C[i])