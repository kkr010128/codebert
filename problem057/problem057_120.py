while 1:
        e=map(int,raw_input().split())
        m=e[0]
        f=e[1]
        r=e[2]
        if m==f==r==-1:
                break
        elif m==-1 or f==-1 or m+f<30:
                print "F"
        elif m+f<50 and r<50:
                print "D"
        elif m+f<65:
                print "C"
        elif m+f<80:
                print "B"
        else:
                print "A"