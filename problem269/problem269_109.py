t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
if a1>b1 and a2>b2:
    print(0)
elif b1>a1 and b2>a2:
    print(0)
elif a1*t1+a2*t2==b1*t1+b2*t2:
    print("infinity")
else:
    ans=-1
    num2=-1
    num3=-1
    if a1*t1+a2*t2>b1*t1+b2*t2:
        if a1>b1:
            ans=0
        else:
            num2=(b1-a1)*t1
            num3=((a1-b1)*t1)+((a2-b2)*t2)
            if num2//num3==num2/num3:
                ans=(num2//num3)*2
            else:
                ans=(num2//num3)*2+1
    else:
        if b1>a1:
            ans=0
        else:
            num2=(a1-b1)*t1
            num3=((b1-a1)*t1)+((b2-a2)*t2)
            if num2//num3==num2/num3:
                ans=(num2//num3)*2
            else:
                ans=(num2//num3)*2+1
    print(ans)
