import sys
import math
H,A = map(int,input().split())

if not ( 1 <= H <= 10**4 and 1 <= A <= 10**4 ): sys.exit()
if not ( isinstance(H,int) and isinstance(A,int)): sys.exit()

print(math.ceil(H/A))