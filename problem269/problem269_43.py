t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
if a1*t1 + a2*t2 == b1*t1 + b2*t2:
    print("infinity")
else:
    A = a1*t1 + a2*t2
    B = b1*t1 + b2*t2
    M1,m1 = max(a1*t1,b1*t1),min(a1*t1,b1*t1)
    M2,m2 = max(A,B),min(A,B)
    gap1,gap2 = M1-m1,M2-m2
    Mv,mv = max(a1,b1),min(a1,b1)
    vgap = Mv-mv
    possible = vgap*t1
    count = possible//gap2
    if possible%gap2 == 0:
        pitta = 1
    else:
        pitta = 0
    if (a1*t1 > b1*t1 and A > B) or (a1*t1 < b1*t1 and A < B):
        print(0)
    elif (a1*t1 > b1*t1 and A < B) or (a1*t1 < b1*t1 and A > B):
        if pitta == 1:
            print(1+count*2-1)
        else:
            print(1+count*2)