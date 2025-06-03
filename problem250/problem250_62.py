n=int(input())
for i in range(n,10**6):
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      break
  else:
    print(i)
    break