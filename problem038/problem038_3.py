x = raw_input().split()
if float(x[0]) < float(x[1]):
    print "a < b"
elif float(x[0]) > float(x[1]):
    print "a > b"
else:
    print "a == b"