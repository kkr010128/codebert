import sys

x = int( sys.stdin.readline() )
h = x//3600
m = ( x%3600 )//60
s = ( x%3600 )%60
print( "{}:{}:{}".format( h, m, s) )