import sys
input=sys.stdin.readline

LEN=2*10**5+10
moves=[0]*LEN
for i in range(1,LEN): #1～Nまでのすべての数について、0になるまでの操作回数を求める
 tmp=i
 cnt=0
 while tmp!=0:
   popcount=0
   for j in range(20):
     if tmp&(1<<j):
       popcount+=1
   tmp%=popcount
   cnt+=1
 moves[i]=cnt

n=int(input())
x=input()
k=x.count('1') 
if k==0: 
   for i in range(n):
       print(1)
elif k==1: 
   pos=x.index('1') 
   for i in range(n):
       if i==pos: 
           print(0)
       else:
           if pos==n-1: 
               print(2)
           else:
               if i==n-1: 
                   print(2)
               else:
                   print(1)
else:
   sum1=0 
   sum2=0 
   tmp1=1
   tmp2=1
   for i in range(n-1,-1,-1): 
       if x[i]=='1':
           sum1+=tmp1
           sum1%=k+1
           sum2+=tmp2
           sum2%=k-1
       tmp1*=2
       tmp1%=k+1
       tmp2*=2
       tmp2%=k-1
   for i in range(n):
       if x[i]=='0': 
           tmp=sum1+pow(2,n-i-1,k+1)
           tmp%=k+1
           print(moves[tmp]+1)
       else: 
           tmp=sum2-pow(2,n-i-1,k-1)
           tmp%=k-1
           print(moves[tmp]+1)