import sys

nums = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
if nums[0] < nums[1]:
	print( "a < b" )
elif nums[0] > nums[1]:
	print( "a > b" )
else:
	print( "a == b" )