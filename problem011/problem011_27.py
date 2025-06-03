z=list(map(int,input().split()))
z.sort()
a=0

while True:
    if z[1]==z[0]:
        break
    a=z[1]-z[0]
    if z[0]%a==0:
        z[1] = z[0]
        z[0] = a
        z.sort()
        break
    z[1]=z[0]
    z[0]=a
    z.sort()

print(z[0])