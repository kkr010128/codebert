import math
n=int(input())
n_=int(math.sqrt(n))

list_ans=[]
for i in range(2,n_+1):
  if n%i==0:
    ans=i+(n//i)-2
    list_ans.append(ans)
    
  
if not list_ans:
  print(n-1)
  exit()
print(min(list_ans))