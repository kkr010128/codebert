n=int(input())

x=list(map(int, input().split()))
y=list(map(int, input().split()))

p1=p2=p3=p4=0
for i in range(n):
    if x[i]>y[i]:
        k=x[i]-y[i]
        p1+=k
        p2+=k**2
        p3+=k**3
        p4=max(p4,k)
        
    else:
        k=y[i]-x[i]
        p1+=k
        p2+=k**2
        p3+=k**3
        p4=max(p4,k)

p2=p2**(1/2)
p3=p3**(1/3)

print(p1,p2,p3,p4, sep="\n")
