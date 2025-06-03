#F
def divisor(n):
  ass = []
  for i in range(1,int(n**0.5)+1):
    if n%i == 0:
      ass.append(i)
      if i**2 == n:
        continue
      ass.append(n//i)
  return ass

n=int(input())
ans1=divisor(n-1)
ans1.remove(1)
as0=divisor(n)
ans0=[]
for x in as0:
  if x!=1:
    m=n
    while m>=x and m%x==0:
      m=m//x
    if m%x==1:
      ans0.append(x)

ans=set(ans0)|set(ans1)
ans=list(ans)




print(len(ans))
"""
ans.sort()
print(ans)
for x in ans:
  m=n
  while m%x==0:
    m=m//x
  print(x,m%x)
"""