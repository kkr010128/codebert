X=list(map(int, input().split()))
t=0
for i in range(len(X)):
  if X[i]==1:
    t+=300000
  elif X[i]==2:
    t+=200000
  elif X[i]==3:
    t+=100000
if X[0]==X[1] and X[0]==1:
  t+=400000
print(t)
