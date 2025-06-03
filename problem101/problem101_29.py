a,b,c = map(int,input().split())
k = int(input())

for i in range(k):
  if(a >= b):
    b*=2
    continue
  if(b >= c):
    c*=2
    continue
    
if(a<b and b<c):
  print("Yes")
  exit()
else:
  print("No")