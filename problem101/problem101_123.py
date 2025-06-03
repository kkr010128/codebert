(r1,g1,b1)=input().split()
(r,g,b)=(int(r1),int(g1),int(b1))
k=int(input())
flg=0
for i in range(k):
  if not g > r :
    g *= 2
  elif not b > g:
    b *= 2

if ( b > g > r):
  print ("Yes")
else:
  print ("No")
  
    
  
