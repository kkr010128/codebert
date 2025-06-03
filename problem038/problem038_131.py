length = raw_input()
a, b = length.split()
 
a = int(a)
b = int(b)

if a < b:
   print "a < b"
elif a == b:
   print "a == b"
elif a > b:
   print "a > b"