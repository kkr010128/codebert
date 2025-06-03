n=int(input())
count=0
countmax=0
for i in range(n):
  a,b = map(int,input().split())
  if a==b:
    count+=1
  else:
    countmax=max(countmax,count)
    count=0
countmax=max(countmax,count)    
if countmax>2:
  print("Yes")
else:
  print("No")
