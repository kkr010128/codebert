import sys
A,B = map(int,input().split())

if not ( 1 <= A <= 20 ): sys.exit()
if not ( 1 <= B <= 20 ): sys.exit()
if not (isinstance(A,int) and isinstance(B,int)): sys.exit()

print(A*B) if A <= 9 and B <= 9 else print(-1)