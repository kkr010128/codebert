k=int(input())
from collections import deque
q=deque([])
i=0
while True:
  if i<=8:
    q.append(i+1)
    i+=1
    if i==k:break
    continue
  
  x=q.popleft()
  
  if x%10!=0:
    q.append(x*10+x%10-1)
    i+=1
    if i==k:break
    
  q.append(x*10+x%10)
  i+=1
  if i==k:break
  
  if x%10!=9:
    q.append(x*10+x%10+1)
    i+=1
    if i==k:break
      
print(q.pop())