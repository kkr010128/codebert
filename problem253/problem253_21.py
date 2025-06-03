n,a,b=map(int,input().split())
if (a-b)%2==0:
  print(abs(a-b)//2)
else:
  if a+b<n+1:
    print(min(a,b)+(abs(a-b)-1)//2)
  else:
    print(min(n+1-a,n+1-b)+(abs(a-b)-1)//2)