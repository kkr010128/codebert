import math

def isPrime( x ):
	if 2 == x or 3 == x:
		return True
	if 0 == x&1:
		return False
	i = 3
	limit = math.sqrt( x )
	while  i <= limit:
		if 0 == x%i:
			return False
		i += 2
	return True
 
 
n = int( raw_input( ) )
nums = []
i = 0
while i < n:
    nums.append( int( raw_input( ) ) )
    i += 1
cnt = i = 0
for val in nums:
    if isPrime( val ):
        cnt += 1
 
print( cnt )