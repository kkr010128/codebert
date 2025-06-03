Ans=[]
i=0
while True:
    l=input().split()
    m=int(l[0])
    f=int(l[1])
    r=int(l[2])
    if m==-1 and f==-1 and r==-1:
        break
    elif m==-1 or f==-1:
        Ans.append("F")
    elif m+f>=80:
        Ans.append("A")
    elif m+f>=65 and m+f<80:
        Ans.append("B")
    elif m+f>=50 and m+f<65:
        Ans.append("C")
    elif m+f>=30 and m<50:
        if r>=50:
            Ans.append("C")
        else:
            Ans.append("D")
    else:
        Ans.append("F")
    i+=1

m=0
while m<i:
    print(Ans[m])
    m=m+1

