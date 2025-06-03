import sys

a, b = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
print( "{} {}".format( a*b, a*2+b*2 ) )