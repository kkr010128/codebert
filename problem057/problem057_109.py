while True:
    m,f,r=map(int,input().split())
    p=m+f
    if m+f+r==-3:
        break
    if m==-1 or f==-1:
        print("F")
    elif p>=80:
        print("A")
    elif 65<=p and p<80:
        print("B")
    elif 50<=p and p<65:
        print("C")
    elif 30<=p and p<50:
        if r>=50:
            print("C")
        else:
            print("D")
    else:
        print("F")