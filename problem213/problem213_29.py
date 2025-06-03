n=int(input())
x=list(map(int,input().split()))
x.sort()
ans,count=[],0

for i in range(x[0],x[-1]+1):
  for j in x:
    count+=(j-i)**2
    
  ans.append(count)
  count=0
  
print(min(ans))