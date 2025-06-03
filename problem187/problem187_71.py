N,X,Y=map(int,input().split())
ANS=[0 for i in range(N-1)]
for i in range(N-1):
  for k in range(i+1,N):
    d=min(k-i,abs(X-i-1)+abs(Y-k-1)+1)
    ANS[d-1]+=1
for i in ANS:
  print(i)