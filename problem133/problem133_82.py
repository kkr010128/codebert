import sys
A,B = map(int,input().split())
if not ( 1 <= A <= 100 and 1 <= B <= 100 ): sys.exit()

print(A*B)