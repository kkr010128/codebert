n,m,k = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

a_sum = [0]
b_sum = [0]
for i in range(n):
  a_sum.append(a_sum[i] + a_list[i])
for i in range(m):
  b_sum.append(b_sum[i] + b_list[i])
 
ans = 0
for i in range(n+1):
  if a_sum[i] > k:
    break
        
  rem = k - a_sum[i]
  while b_sum[m] > rem:
    m -= 1
  if ans < i + m:
    ans = i + m
        
print(ans)
