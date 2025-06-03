a = input()
for i in xrange(10000) :
    print "Case " + str(i+1) + ": " + str(a)
    a = input()
    
    if (a == 0) :
        break