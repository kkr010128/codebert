d=raw_input().split(" ")
l=list(map(int,d))
if(l[2]>0 and l[3]>0):
    if(l[0]>=(l[2]+l[4])):
        if(l[1]>=(l[3]+l[4])):
            print "Yes"
        else:
            print "No"
    else:
        print "No"
else:
   print "No"
