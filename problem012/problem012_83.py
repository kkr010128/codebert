def isPrime( x ):
	if 2 == x or 3 == x:
		return True
	if 0 == x%2:
		return False
	i = 3 
	while  i*i <= x:
		if 0 == x%i:
			return False
		i += 1
	return True


n = int( raw_input( ) )
nums = []
i = 0
while i < n:
	nums.append( int( raw_input( ) ) )
	i += 1
cnt = i = 0
for num in nums:
	if isPrime( num  ):
		cnt += 1
	i += 1

print( cnt )