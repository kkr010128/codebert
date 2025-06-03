n=int(input())
l=list(map(int,input().split()))
s=sum(l)//n
k=1+(sum(l)//n)
c=0
x=0
for i in range(n):
    c+=(l[i]-s)**2
for i in range(n):
    x+=(l[i]-k)**2
print(min(c,x))
