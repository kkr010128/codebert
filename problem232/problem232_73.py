a,b=map(int,input('').split(' '))
if a<=b:
    s=''
    for i in range(b):
        s=s+str(a)

    print(s)

elif b<a:
    s=''
    for i in range(a):
        s=s+str(b)
    
    print(s)