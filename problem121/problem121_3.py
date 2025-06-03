n=int(input())

def ans(x):
  a=26
  b=1
  k=1
  ch=0
  while ch==0:
    
    if b<= x <= b+a**k-1:
      ch+=1
      return k,x-(b-1)
    else:
      b=b+a**k
      k+=1

s,t=ans(n)
ans1=''
c='abcdefghijklmnopqrstuvwxyz'
for i in range(1,s+1):
  q=0
  f=26**(s-i)
  if i!=s:
    cc=0
    while cc==0:
      e=t-f*(q+1)
      if e>0:
        q+=1
      else:
        cc+=1
      if q==25:
        break
    t-=f*q
    g=c[q]
    ans1=ans1+g
    
  else:
    g=c[t-1]
    ans1=ans1+g
      
print(ans1)