n = int(input())
a = [0 for _ in range(n+1)]
for i in range(1,n+1):
  if i*i>n:
    break
  for j in range(1,n+1):
    if i*i + j*j +i*j > n:
      break
    for k in range(1,n+1):
      tmp = i*i + j*j + k*k + i*j + j*k + k*i
      if tmp<=n:
        a[tmp]+=1
      else:
        break
for i in range(1,n+1):
  print(a[i])