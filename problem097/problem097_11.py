K = int(input())
 
if K % 2 == 0:
  print(-1)
  exit()

num = 0
for i in range(1, K+1):
  num = (num*10+7) % K
  if num == 0:
    print(i)
    exit()

print(-1)