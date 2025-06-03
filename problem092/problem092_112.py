X,K,D=input().split(' ')
x,k,d=abs(int(X)),int(K),int(D)

x_par=x%d
x_num=int((x-x_par)/d)

s=0
if x_num<=k:
  x_div=x-x_num*d
  k-=x_num
  if k%2==0:
    s=abs(x_div)
  else:
    s=x_div-d
else:
  s=x-d*k
print(abs(s))