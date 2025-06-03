N = int(input())
n = round(N**0.5)
counter = [0]*N
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      f = i**2+j**2+k**2+i*j+j*k+k*i
      if f <= N:
        counter[f-1] += 1
for i in range(N):
  print(counter[i])