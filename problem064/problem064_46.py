str1 = raw_input()
str2 = raw_input()
n = len(str1)

for i in xrange(n):
    j = i
    s = 0
    for k in xrange(len(str2)):
        if (j+k) > (n-1):
            j = -k
        if str1[j+k] != str2[k]:
            s += 1
    if s == 0:
        print "Yes"
        break
else:
    print "No"