a,b,c,d = map(int,input().split())
ans=[]
for X in [a,b]:
  for Y in [c,d]:
    ans.append(X*Y)
print(max(ans))
