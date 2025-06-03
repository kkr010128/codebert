n=int(input())
lis=[]
count=0
high=0
for _ in range(n):
  lis.append(input().split())
lis.append([5,6])  
for i in range(n+1):
  if lis[i][0]==lis[i][1]:
    count+=1
  else:
    if count>=high:
      high=count
    count=0
    
if high>=3:
  print("Yes")
else:
  print("No")