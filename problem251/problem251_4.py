n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

t2 = [[] for _ in range(k)]
score = [0]*n
for i,c in enumerate(t):
  t2[i%k].append(c)
score = {'r':p,'s':r,'p':s}
total = 0
for t3 in t2:
  if len(t3)==0: continue
  if len(t3)==1:
    total += score[t3[0]]
    continue  
  for i in range(len(t3)-1):
    if t3[i] == 'e': continue
    total += score[t3[i]]
    if t3[i] == t3[i+1]:
      t3[i+1]='e'
  if t3[-1] != 'e':
    total += score[t3[-1]]
print(total)
