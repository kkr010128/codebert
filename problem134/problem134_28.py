n = int(input())
arr = list(map(int,input().split()))
res = 1
flag = 1
arr.sort()
inf = int(1e18)
for i in range(n):
  res = res*arr[i]
  if(res > inf):
    flag = 0
    break
 
if(flag == 0):
  print(-1)
else:
  print(res)