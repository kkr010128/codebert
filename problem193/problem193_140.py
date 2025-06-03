h,*s=open(0)
h,w,k,*m=map(int,h.split())
b=512
while b:
 b-=1;r=t=j=0;d=[0]*h
 while w-j:
  i=c=0
  while h-i:
   d[c]+=s[i][j]>'0';f=d[c]>k
   if(t<j)&f:r+=1;t=j;d=[0]*h;break
   r+=h*w*f;c+=b>>i&1;i+=1
  else:j+=1
 m+=r+bin(b).count('1'),
print(min(m))