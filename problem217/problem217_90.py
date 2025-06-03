a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
  if b[i]%2==0:
    if b[i]%3==0 or b[i]%5==0:
      c=c+1
  else:
    c=c+1
if c==a:
  print("APPROVED")
else:
  print("DENIED")