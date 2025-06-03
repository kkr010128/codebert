a = int ( input ( ) )

h = a // 3600
m = ( a // 60 ) % 60
d = a % 60
print ( "%s:%s:%s" % ( h, m, d ) )