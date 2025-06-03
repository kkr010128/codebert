t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

a=a1-b1
b=a2-b2

if a<=0:
    a *= -1
    b *= -1

X=t1*a
Y=t2*b


if X+Y==0:
    print('infinity')
elif X+Y>0:
    print(0)
else:
    T=X//abs(X+Y)
    if X%abs(X+Y)==0:
        print(T*2)
    else:
        print(T*2+1)
