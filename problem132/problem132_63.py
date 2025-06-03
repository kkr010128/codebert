import math
n,k=map(int,input().split())
  
a=[0]*n
ans=[0]*n
a=list(map(int,input().split()))
check=math.ceil(math.log2(n))+1
if (k>=42):
  a=[n]*n
  print(" ".join(map(str,a)))
else:
  for _ in range(k):
    ans=[0]*n
    table=[0]*n
    for i in range(n):
      left=max(0,i-a[i])
      right=min(n-1,i+a[i])
      table[left]+=1
      if (right+1<n):
        table[right+1]-=1
      #print(left,right)
      #for j in range(left,right+1):
      #  ans[j]+=1
    #print(table)
    for i in range(1,n):
      table[i]+=table[i-1]
    a=table
 
  print(" ".join(map(str,a)))