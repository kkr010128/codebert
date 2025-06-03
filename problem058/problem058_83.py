import sys

while True:
	n, x = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 == n and 0 == x:
		break
		
	cnt = 0
	ave = x // 3
	for i in range( 1, ave ):
		ave2 = (x-i) // 2
		for j in range( i+1, ave2+1 ):
			k = x-i-j
			if j < k and k <= n:
				cnt += 1
	
	print( cnt )