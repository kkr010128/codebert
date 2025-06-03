import fileinput
for i, line in enumerate(fileinput.input()):
    x = line.strip()
    if x != '0':
        print "Case %d: %s" % (i + 1, x)
    else:
        break