v=raw_input()
a=int(v[:v.find(" ")])
b=int(v[v.find(" "):])
if(a>b):
    print "a > b"
elif(a<b):
    print "a < b"
else:
    print "a == b"
