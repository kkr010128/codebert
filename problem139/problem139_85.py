h1,m1,h2,m2,k=map(int,input().split())
r=((h2-h1)*60)+m2-m1-k
if r>=0:
  print(r)
else:
  print(0)