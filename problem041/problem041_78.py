X= raw_input().split()
if float(X[2]) + float(X[4]) <= float(X[0])and float(X[2]) - float(X[4]) >= 0 and float(X[3]) + float(X[4]) <= float(X[1]) and float(X[3]) - float(X[4]) >= 0:
    print "Yes"
else:
    print "No"        