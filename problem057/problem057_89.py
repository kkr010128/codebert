while 1:
    m,f,r=map(int, raw_input().split())
    if m==f==r==-1: break
    s=m+f
    if m==-1 or f==-1 or s<30: R="F"
    elif s>=80: R="A"
    elif s>=65: R="B"
    elif s>=50: R="C"
    elif r>=50: R="C"
    else: R="D"
    print R