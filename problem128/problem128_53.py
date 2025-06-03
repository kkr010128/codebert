x,n=map(int,input().split())
if n==0:
  print(x)
  exit()
p=list(map(int,input().split()))
p.sort()
t=0
while True:
  if x-t in p and x+t in p:
    t+=1
  elif x-t in p and x+t not in p:
    print(x+t)
    exit()
  elif x-t not in p:
    print(x-t)
    exit()