N = int(input())

ans = [0]*10050

for i in range(1,105):
  for j in range(1,105):
    for k in range(1,105):
      v = (i+j+k)**2-(i*j+i*k+j*k)
      if v < len(ans):
        ans[v] += 1
  
for x in range(1,N+1):
  print(ans[x])