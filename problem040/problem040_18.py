#coding:utf-8
import sys
 
abc=sys.stdin.readline()
nums=abc.split( ' ' )
for i in range( len( nums) ):
	nums[i] = int( nums[i] )
nums.sort()
print( "{} {} {}".format( nums[0], nums[1], nums[2] ) )