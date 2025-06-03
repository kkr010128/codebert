a,b=map(int,input().split())
x=str(a)*b
y=str(b)*a
for i in range(len(min(x,y))):
  if x[i]<y[i]:
    print(x)
    break
  elif x[i]>y[i]:
    print(y)
    break
if x==y:
  print(x)