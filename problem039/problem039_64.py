length = raw_input()
a, b, c = length.split()
 
a = int(a)
b = int(b)
c = int(c)

if a < b and b < c:
   print "Yes"
else:
   print "No"