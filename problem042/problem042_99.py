import sys

i=1
while True:
    x = sys.stdin.readline().rstrip() 
    if "0" != x:
        print( "Case {}: {}".format( i, x) )
    else:
        break
    i += 1