mf = 0
while True:
    m,f,r = [int(i) for i in input().strip().split()]
    if m==f==r==-1 : break
    mf = m+f

    if m*f<0 or mf<30 : print("F")
    elif mf<50 and r<50 : print("D")
    elif mf<65 : print("C")
    elif mf<80 : print("B")
    elif mf>=80 : print("A")
    else: print("F")