n=int(input())
sum=0

for i in range(n+1):
  if i%3==0 or i%5==0:
    sum+=0
  else:
    sum+=i

print(sum)