N=int(input())
f=[0]*10000
for i in range(100):
  for j in range(100):
    for k in range(100):
      n=(i+1)**2+(j+1)**2+(k+1)**2+(i+1)*(j+1)+(j+1)*(k+1)+(k+1)*(i+1)  
      if n<=10000:
        f[n-1]+=1
for i in range(N):
  print(f[i])
