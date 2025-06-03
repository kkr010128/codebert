a=input().split()
n=(int)(a[0])
q=(int)(a[1])
b=[0 for i in range(2*n)]
cnt=0
tmp=0
for i in range(n):
    B=input().split()
    b[2*i]=B[0]
    b[2*i+1]=int(B[1])
while len(b)>0:
    tmp=b[1]-q
    if tmp>0:
        b.append(b[0])
        b.append(tmp)
        del b[0]
        del b[0]
        cnt=cnt+q
    else:
        cnt=cnt+b[1]
        print(b[0],cnt)
        del b[0]
        del b[0]
