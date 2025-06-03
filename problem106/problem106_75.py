n = int(input())
ans = [0]*n

for i in range(1,101):
  for j in range(1,101):
    for k in range(1,101):
      l = i**2 + j**2 + k**2 + i*j + j*k + k*i
      if l <= n:
        ans[l-1] += 1
      
for m in range(n): 
  print(ans[m])