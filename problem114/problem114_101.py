D=int(input())
c=list(map(int,input().split()))
last=[0 for i in range(26)]
cost=[0 for i in range(26)]
degree=[0 for i in range(26)]
score=0
s=[]
t=[]
for _ in range(D):
  s.append(list(map(int,input().split())))
for _ in range(D):
  t.append(int(input()))
for d in range(D):
  for i in range(26):
    cost[i]+=c[i]*(d+1-last[i])
  k=t[d]-1
  cost[k]-=c[k]*(d+1-last[k])
  last[k]=d+1
  score+=s[d][k]
  print(score-sum(cost))