import sys

n = int( sys.stdin.readline() )
nums = sys.stdin.readline().rstrip().split( " " )
nums.reverse()
print( " ".join( nums ) )