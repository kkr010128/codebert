a=input().split(' ')
a[0]=int(a[0])
a[1]=int(a[1])
a[2]=int(a[2])
c=a[0]
m=0
while c<a[1]+1:
    if c%a[2]==0:
        m=m+1
    c=c+1
print(m)
