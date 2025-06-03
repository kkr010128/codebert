k=int(input())
flag=0
s=0
for i in range(1,9*k):
   s+=7
   s%=k
   if s==0:
       flag=i
       break
   s*=10
    
if flag:
    print(flag)
else:
    print(-1)
