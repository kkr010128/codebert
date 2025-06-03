N,M = map(int,input().split())
a = [0]*N
b = [None]*N
for i in range(M):
  s,c = map(int,input().split())
  if b[s-1] == c:
    continue
  else:
    a[s-1] +=1
    b[s-1] =c
    
count = 0
for i in range(N):
  if a[i]>=2:
    count=-1
  elif b[0]==0 and N>1:
    count =-1
  elif i==0:
    if b[i] is None:
      if N==1:
        b[i] =0
      else:
        b[i]=1
  elif i>0:
    if b[i] is None:
      b[i]=0
b.reverse()
if count == 0:
  for i in range(N):
    count+=b[i]*10**i
print(count)