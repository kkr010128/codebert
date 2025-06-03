
#atcoder 
t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

d1=a1-b1
d2=a2-b2

if d1*d2>0:
    print(0)
else:
    if d1>0 and d2<0:
        plus=d1*t1+d2*t2
        if plus>0:
            print(0)
        elif plus==0:
            print("infinity")
        elif plus<0:
            d=-plus
            k=d1*t1
            if k%d==0:
                print(2*k//d)
            else:
                print(2*(k//d)+1)
    else:
        d1=-d1
        d2=-d2
        plus=d1*t1+d2*t2
        if plus>0:
            print(0)
        elif plus==0:
            print("infinity")
        elif plus<0:
            d=-plus
            k=d1*t1
            if k%d==0:
                print(2*k//d)
            else:
                print(2*(k//d)+1)
