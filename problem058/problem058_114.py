import sys

while True:
	n, x = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 == n and 0 == x:
		break
		
	cnt = 0
	goto = False
	for i in range( 1, n-1 ):
		if  x < 3*(i+1):
			break
		for j in range( i+1, n ):
			if  x <= ( i+j ):
				break
			for k in range( j+1, n+1 ):
				s = ( i + j + k )
				if x == s:
					cnt += 1
					break
				elif   x < s:
					goto = True
					break
			goto = False
	
	print( cnt )