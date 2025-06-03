while 1:
        c=list(raw_input())
        o=""
        if c[0]=="-" and len(c)==1:
                break
        m=int(raw_input())
        for i in range(m):
                h=int(raw_input())
                c=list(c[h:]+c[:h])
        for i in range(len(c)):
                o+=c[i]
        print o