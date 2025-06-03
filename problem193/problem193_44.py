h,*s=open(0)
h,w,k,*m=map(int,h.split())
b=w
while b:
 b-=1;r=t=j=0;d=[0]*h
 while w-j:
  i=c=0;j+=1
  while h-i:
   d[c]+=s[i][~j]>'0'
   if d[c]>k:d=[0]*h;f=t<j;r-=h*w*~-f-1;t=j;j-=f;break
   c+=b>>i&1;i+=1
 m+=r+c,
print(min(m))