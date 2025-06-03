x = 0
while x == 0:

 m = map(int,raw_input().split())

 if m[0] == 0 and m[1] == 0:
     break

 for i in xrange(m[0]):
    print "#" * m[1]
 print ""