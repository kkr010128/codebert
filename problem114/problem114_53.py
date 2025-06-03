D=int(input())
c=list(map(int,input().split()))
s=[]
for i in range(D):
  s.append(list(map(int,input().split())))
t=[]
for i in range(D):
  t.append(int(input()))
last_di=[0]*26
m=0
for i in range(D):
  m+=s[i][t[i]-1]
  last_di[t[i]-1]=i+1
  for j in range(26):
    m-=c[j]*((i+1)-last_di[j])
  print(m)
