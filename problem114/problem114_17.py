D=int(input())
c=[int(x) for x in input().split()]
s=[[0]*i for i in range(D)]
t=[]
last_d=[0]*26
for i in range(D):
  s[i]=[int(x) for x in input().split()]
for i in range(D):
  t.append(int(input()))

v=0
for i in range(D):
  a=0
  for j in range(26):
    if j!=t[i]-1:
      n=i+1-last_d[j]
      a+=c[j]*n
  v=v+s[i][t[i]-1]-a
  print(v)
  last_d[t[i]-1]=i+1