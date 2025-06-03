A,B=map(int,input().split())

for x in range(1,1001):
  if A==int(x*0.08) and B==int(x*0.1):
    print(x)
    break
  elif x==1000:
    print(-1)
