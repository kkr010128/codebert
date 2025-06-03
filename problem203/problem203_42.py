a,b=[int(x) for x in input().split()]
c=0
for i in range(1,12501):
  if int(0.08*i)==a and int(0.1*i)==b:
    ans=i
    c=1
    break
if c==1:
  print(ans)
else:
  print(-1)