n=int(input())
ans=0
for i in range(1000):
  ans=n+i
  if ans%1000==0:
    print(i)
    break