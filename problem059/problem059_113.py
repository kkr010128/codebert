r,c = map(int,raw_input().split())
cels = []
for i in xrange(r):
    cols = map(int, raw_input().split())
    cels.append(cols)

for i in xrange(r):
    cels[i].append(sum([ j for j in cels[i]]))

sum_c=[]
for i in xrange(c):
    sum_c.append(sum([cels[n][i] for n in xrange(r)]))

cels.append(sum_c)
cels[r].append(sum(cels[r]))

for i in xrange(r+1):
    print " ".join(map(str,cels[i]))