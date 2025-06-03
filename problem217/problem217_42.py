N=int(input())
A=list(map(int,input().split()))
b=0
for x in A:
  if x%2==0:
    if x%3==0 or x%5==0:
      pass
    else:
      b=1
      break
if b==0:
  print("APPROVED")
else:
  print("DENIED")