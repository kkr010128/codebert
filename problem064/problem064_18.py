s = raw_input()
p = raw_input()

slen = len(s)
plen = len(p)
flag = False

for i in xrange(len(s)):
    j = 0
    while(j < plen and s[(i+j)%slen] == p[j]):
        j += 1
    if (j == plen):
        flag = True

if(flag):
    print "Yes"
else:
    print "No"