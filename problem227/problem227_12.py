N,K=map(int,input().split())
H=list(map(int, input().split()))
#Nモンスターの数、K必殺回数（モンスターは体力ゼロになる）、Hモンスターの数と各々の体力
H=sorted(H)
if K>=len(H):
  print(0)
else:
  for i in range(0,K):
    del H[-1]
  result=sum(H)
  print(result)