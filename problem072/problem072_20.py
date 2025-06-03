N=int(input())
D=[map(int, input().split()) for i in range(N)]
x, y = [list(i) for i in zip(*D)]

s=0
l=[]
for i in range(N):
  if x[i]==y[i]:
    s+=1
    if i==N-1:
      l.append(s)
  elif x[i]!=y[i]:
    l.append(s)
    s=0

if max(l)>=3:
  print("Yes")
else:
  print("No")