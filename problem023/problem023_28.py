n = int(raw_input())
d = {}
for i in range(n):
    p,q = map(str,raw_input().split())
    if p == "insert":
        d[q] = 1
    elif p == "find":
        if(q in d):
            print "yes"
        else:
            print "no"