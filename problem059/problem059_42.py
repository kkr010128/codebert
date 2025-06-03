l=input().split()
r=int(l[0])
c=int(l[1])

# for yoko
i=0
b=[]
while i<r:
    a=input().split()
    q=0
    su=0
    while q<c:
        b.append(int(a[q]))
        su+=int(a[q])
        q=q+1
    b.append(su)
    i=i+1

# for tate
#x=0
#d=b[0]+b[c+1]+b[2*(c+1)]+b[3*(c+1)]
#x<c+1
x=0
while x<c+1:
    d=0
    z=0
    while z<r:
        d+=b[x+z*(c+1)]
        z+=1
    b.append(d)
    x=x+1
# for output
# C=[]
# y=0 (for gyou)
# z=0 (for yoko)
C=[]
y=0
while y<r+1:
    z=0
    Ans=str(b[y*(c+1)+z])
    while z<c:
        z+=1
        Ans=Ans+" "+str(b[y*(c+1)+z])
    C.append(Ans)
    y+=1

for k in C:
    print(k)

