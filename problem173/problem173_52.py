N=int(input())
a=1
sum=0
while a in range(N+1):
  if a%3 !=0 and a%5 !=0:
    sum=sum+a
    a = a + 1
  else:a=a+1
print(sum)
