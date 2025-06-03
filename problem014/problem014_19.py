n=int(input())
a=list(map(int,input().split()))
c=0;b=1;i=0
while b:
 b=0
 for j in range(0,n-i-1):
  if a[j]>a[j+1]:a[j],a[j+1]=a[j+1],a[j];b=1;c+=1
 i+=1
print(*a)
print(c)
