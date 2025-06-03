n, m, k = map(int, input().split(' '))
list_a = list(map(int, input().split(' ')))
list_b = list(map(int, input().split(' ')))
 
a_sum=[list_a[0]]
for i in range(1, n):
  a_sum.append(list_a[i]+a_sum[i-1])
  
b_sum=[list_b[0]]
for i in range(1, m):
  b_sum.append(list_b[i]+b_sum[i-1])

  
ans=0 
if (a_sum[0]>k) and (b_sum[0]>k):
  print(0)
else:
  for j in range(m):
    if b_sum[j]<=k:
      ans=max(ans, j+1)
  j=m-1
  for i in range(n):
    if a_sum[i]<=k:
      ans=max(ans, i+1)
      while a_sum[i] + b_sum[j] > k and j>0:
        j-=1
      if a_sum[i]+b_sum[j]<=k:
        ans=max(ans, i+j+2)
  print(ans)