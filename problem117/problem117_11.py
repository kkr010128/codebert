def judge(num):
  if num>n+m:
    return False
  for i in range(max(0,num-m),min(n,num)+1):
    if a_cumsum[i] + b_cumsum[num-i]<=k:
      return True
  return False
 
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
a_cumsum = [0]
b_cumsum = [0]
for i in a:
  a_cumsum.append(a_cumsum[-1]+i)
for i in b:
  b_cumsum.append(b_cumsum[-1]+i)
  
left = 0
right = k+1
 
while right-left>1:
  mid = (right+left)//2
  
  if judge(mid):
    left = mid
  else:
    right = mid
 
print(left)