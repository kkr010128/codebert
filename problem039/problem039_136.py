i = raw_input().strip().split()
 
a = int(i[0])
b = int(i[1])
c = int(i[2])

if a < b and b < c:
    print "Yes"
else:
    print "No"