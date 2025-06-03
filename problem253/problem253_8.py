n,a,b=map(int,input().split())
if (a+b)%2==0:print(abs(a-b)//2)
else:
  aa,bb=1,b-a
  ans=a+abs(b-a)//2
  aa,bb=a+(n-b+1),n
  ans=min((n-b+1)+abs(b-a)//2,ans)
  print(ans)