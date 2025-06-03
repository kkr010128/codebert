N = int(input())
c = 0
for i in range(1,N):
  if i**2 >= N:
    break
  c += 1
for i in range(1,N):
  for j in range(i+1,N):
    if i*j >= N:
      break
    c += 2
print(c)