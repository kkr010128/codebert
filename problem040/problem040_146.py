import sys

nums = sorted( [ int( val ) for val in sys.stdin.readline().split( " " ) ] )
print( "{:d} {:d} {:d}".format( nums[0], nums[1], nums[2] ) )	