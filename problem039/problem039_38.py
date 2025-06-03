import sys

nums = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
if nums[0] < nums[1] and nums[1] < nums[2]:
	print( "Yes" )
else:
	print( "No" )