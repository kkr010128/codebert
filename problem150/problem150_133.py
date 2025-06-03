import sys

n,k=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    a[i]-=1
#print(a)

if k<=n:
    b=0
    for i in range(k):
        b=a[b]
    print(b+1)
    sys.exit()
    
b=0
c=[-1]*n
c[0]=0
for i in range(n):
#   print(b,a[b])
   b=a[b]
   if c[b]>=0:
#       print("i:",i)
       break
   else:
       c[b]=i+1

ki=c[b]+1
kc=(i+1)-c[b]
k2=(k-ki)%kc+ki
#print("ki:",ki,"kc:",kc,"k2:",k2)
b=0
for i in range(k2):
    b=a[b]
print(b+1)
