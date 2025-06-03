X,K,D=map(int, input().split())

if 0<abs(X)<K*D:
  a=X//D
  K-=a
  if K%2==0:
    ans=X-D*a
  else:
    ans=X-D*(a+1)

else:
  ans=abs(X)-K*D
    
print(abs(ans))