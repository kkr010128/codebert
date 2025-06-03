import sys
A1,A2,A3 = map(int,input().split())
if not ( 1 <= A1 <= 13 and 1 <= A2 <= 13 and 1 <= A3 <= 13 ): sys.exit()
if not ( isinstance(A1,int) and isinstance(A2,int) and isinstance(A3,int) ): sys.exit()
print('bust') if A1 + A2 + A3 >= 22 else print('win')