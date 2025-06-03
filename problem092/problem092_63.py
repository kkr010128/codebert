x,k,d=map(int,input().split())
x=abs(x)
if k>=round(x/d):
  if (k-round(x/d))%2==0:
    print(abs(x-d*round(x/d)))
  else:
    print(d-abs(x-d*round(x/d)))
else:
  print(x-d*k)