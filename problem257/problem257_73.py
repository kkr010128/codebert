N = int(input())
a = list(map(int,input().split()))

check = 1
ans = 0


for i in a:
  ans+=1
  if i == check:
    ans -=1
    check+=1
    
if a==[j for j in range(1,N+1)]:
  print(0)
  exit()
  
elif ans==N:
  print(-1)
  exit()

print(ans)
  
  

