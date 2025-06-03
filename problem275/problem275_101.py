x,y = map(int, input().split())

ans=0
if x==1 and y==1:
  ans+=400000

def get(i):
  if i==1:
    return 300000
  if i==2:
    return 200000
  if i==3:
    return 100000
  return 0

print(ans+get(x)+get(y))