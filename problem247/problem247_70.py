import fractions
N,M=map(int,input().split())
a=list(map(int,input().split()))
l=1
count=0
A=a[0]
ans=0
flag=1
while A%2==0:
    A=A//2
    count=count+1
for i in range(N):
    A=a[i]
    b=A//(2**count)
    if b==0 or b%2==0:
        flag=0
        break
    A=A//2
    l=l*A//fractions.gcd(l,A)
if flag==1:
    ans=M//l
    if ans%2==0:
        print(ans//2)
    else:
        print(ans//2+1)
else:
    print(0)