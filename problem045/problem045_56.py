l=raw_input()
k=l.split()
a=0.0
b=0.0
a=int(k[0])
b=int(k[1])
#
print int((a-(a%b))/b),
print int(a%b),
a*=1.0
b*=1.0
if b==1:
        print a*1.0
else:
        if a/b>0.0000002:
                print a/b
        else:   print "0.00000001.99999982"