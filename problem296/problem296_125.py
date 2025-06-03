A=list(input())
n=int(input())
tmp=0
if len(set(A)) == 1:
   print(len(A)*n//2)
   exit()
sum_n=0
tmp3=0
while A[0] == A[tmp3]:
   tmp3+=1
sum_n+=tmp3
tmp3=0
while A[-1] == A[-1-tmp3]:
   tmp3+=1
sum_n+=tmp3
for i in range(len(A)-1):
   if A[i] == A[i+1]:
      A[i+1]="1"
      tmp+=1
tmp2=0
if A[0] == A[-1]:
   tmp2=n-1
   if sum_n%2 == 1:
      tmp2-=n-1
print(tmp*n+tmp2)