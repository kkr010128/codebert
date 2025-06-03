a,b,k=map(int,input().split())
if a>k:
  a=a-k
  b=b
elif a+b<=k:
  b=0
  a=0
elif a<=k:
  b=b+(a-k)
  a=0
print(a,b)
