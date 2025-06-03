import sys
n = int(input())
a = list(map(int,input().split()))

ans = 0
if 1 not in a:
  print(-1)
  sys.exit()
  
index = 1
for i in a:
  if i != index:
    ans+=1
  else:
    index+=1
    
print(ans)
