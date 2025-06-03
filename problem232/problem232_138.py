a, b = (int(x) for x in input().split())
ans=0
if a==b:
  for i in range(a):
    ans+=a*pow(10,i)
elif a>b:
  for i in range(a):
    ans+=b*pow(10,i)
else:
  for i in range(b):
    ans+=a*pow(10,i)
print(ans)