n=int(input())
a=[0]*10001
for i in range(1,101):
  for j in range(1,101):
    for k in range(1,101):
      v=i**2+j**2+k**2+i*j+j*k+k*i
      if v<10001:
        a[v]+=1
for m in range(n):
  print(a[m+1])