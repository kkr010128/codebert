import sys

w = sys.stdin.readline().rstrip().lower()
cnt = 0
while True:
    lines = sys.stdin.readline().rstrip()
    if not lines:
		break	
    words = lines.split( " " )
    for i in range( len( words ) ):
    	if w == words[i].lower():    		
			cnt += 1			
print( cnt )