import sys

s = sys.stdin.readline().rstrip()
s += s
pstr = sys.stdin.readline().rstrip()
if  pstr in s:
	print( "Yes" )
else:
	print( "No" )