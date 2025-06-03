import string
L = string.split(raw_input())
a = int(L[0])
b = int(L[1])

if a == b:
    print "a == b"
    
elif a > b:
    print "a > b"
    
elif a < b:
    print "a < b"