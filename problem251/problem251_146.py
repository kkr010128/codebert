N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
r =[0]*100001
s=[0]*100001
p=[0]*100001
for i in range(N):
  if T[i]=='r':
    r[i]=1
    if i>=K:
      if r[i-K]==1:
        r[i]=0
  elif T[i] =='s':
    s[i]=1
    if i>=K:
      if s[i-K]==1:
        s[i]=0
  elif T[i]=='p':
    p[i]=1
    if i>=K:
      if p[i-K]==1:
        p[i]=0
count=0
for i in range(N):
  if r[i]==1:
    count+=P
  elif s[i]==1:
    count+=R
  elif p[i]==1:
    count+=S
print(count)
    
