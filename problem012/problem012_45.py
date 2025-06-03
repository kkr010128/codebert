import math
 
def prime(num):
  if num==1 or num==2 or num==3:
    return True
  for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
      return False
  else:
    return True
 
n=int(input())
ans=0
for i in range(n):
  tmp=int(input())
  if prime(tmp):
    ans+=1
print(ans)
