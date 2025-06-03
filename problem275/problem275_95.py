def keisan(x):
  if x==1:
    return 300000
  elif x==2:
    return 200000
  elif x==3:
    return 100000
  else:
    return 0

X,Y=map(int,input().split())
ans=keisan(X)+keisan(Y)
if X==Y==1:
  ans+=400000
print(ans)
