n=int(input())
ans=set()
ans.add(n)
i=2
x = 1
while x * x <= n-1 :
  if (n-1) % x == 0:          
    ans.add(x)
    ans.add((n-1)//x)
  x += 1
while i*i<=n:
  t=n
  while t%i==0:
    t/=i
  if t%i==1:
    ans.add(i)
  i+=1
print(len(ans)-1)