N=int(input())
Alist=list(map(int,input().split()))
ans=0
for i in range(N):
  if Alist[i]%2==0:
    if Alist[i]%3!=0 and Alist[i]%5!=0:
      ans=1
      break
print("APPROVED"*(1+(-1)*ans)+"DENIED"*ans)