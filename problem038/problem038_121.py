x = raw_input().split()
m = map(int,x)

a = m[0]
b = m[1]

if a > b:
    print "a > b"
elif a < b:
    print "a < b"
else:
    print "a == b"