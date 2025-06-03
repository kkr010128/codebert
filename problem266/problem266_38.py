X=int(input())
DP=[0 for i in range(X+1)]
DP[0]=1
L=[100,101,102,103,104,105]

for s in range(6):
  for x in range(X+1):
    if DP[x]==1 and x+L[s]<=X:
      DP[x+L[s]]=1
print(DP[X])