b=input().split(' ')
b[0]=int(b[0])
b[1]=int(b[1])
k=1
m=0
while k==1:
    if b[0]<=0:
        k=k+1
    b[0]=b[0]-b[1]
    m=m+1
print(m-1)