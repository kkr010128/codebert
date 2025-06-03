import sys

while True:
	xy=sys.stdin.readline()
	nums=xy.split( ' ' )
	for i in range( len( nums) ):
		nums[i] = int( nums[i] )
	if nums[0] == 0 and nums[1] == 0:
		break
	else:
		if nums[1] < nums[0]:
			t=nums[0]
			nums[0]=nums[1]
			nums[1]=t
		print( "{} {}".format( nums[0], nums[1] ) )