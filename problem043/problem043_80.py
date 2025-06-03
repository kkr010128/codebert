
l=raw_input()
k=l.split()
k.sort()
f=0
#
while f==0:
        a=int(k[0])
        b=int(k[1])
        if a==b==0:
                break
        else:
                if a<b:
                        print a,b
                else:
                        print b,a
        l=raw_input()
        k=l.split()
        k.sort()