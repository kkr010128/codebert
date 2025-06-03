n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

a=0
for i in range(n):
    a+=abs(x[i]-y[i])
print('{:.6f}'.format(a))

b=0
for i in range(n):
    b+=(x[i]-y[i])**2
print('{:.6f}'.format(b**(1/2)))

c=0
for i in range(n):
        c+=abs((x[i]-y[i]))**3
print('{:.6f}'.format(c**(1/3)))

d=[]
for i in range(n):
    d.append(abs(x[i]-y[i]))
print('{:.6f}'.format(max(d)))
    
