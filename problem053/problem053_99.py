import sys

n = int( sys.stdin.readline() )
nums = sys.stdin.readline().rstrip().split( " " )
nums.reverse()
output = []
for i in range( n ):
	output.append( nums[i] )
	if i < (n-1):
		output.append( " " )
print( "".join( output ) )