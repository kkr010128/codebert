a,b,c,k=map(int,input().split())
if k<=a:
  ans=k
elif k>a and k<=a+b:
  ans=a
else:
  ans=a-(k-(a+b))
print(ans)