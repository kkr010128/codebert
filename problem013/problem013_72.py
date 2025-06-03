n=input()
min = None
max = None
cand=None

for x in xrange(n):
    v = input()
   
    # print "#### %s %s %s %s" % (str(max), str(min), str(cand), str(v))

    if min is None:
        min = v
        # print "min is None"
        continue

    if min > v:
        # print "min > v"
        if (cand is None) or (cand < v-min):
            # print "cand None"
            cand = v-min
        min = v
        max = None
        continue

    elif (max is None) or (max < v):
        # print "max is None"
        max = v
        if cand < max - min:
            cand = max - min
        continue

print cand