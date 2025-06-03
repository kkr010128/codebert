x=list(map(int, input().split()))
L=x[0]
R=x[1]
d=x[2]
res=0
while L<=R:
  if L%d==0:
    res+=1
  L+=1
print(res)