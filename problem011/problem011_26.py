tmp=input().split()
m=int(tmp[0])
n=int(tmp[1])

while(m!=n):
    if(m>n):
        m=m-n
    else:
        n=n-m

print(m)