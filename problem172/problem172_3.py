import sys
N = int(input())
strN = str(N)

if not ( 100 <= N <= 999 ): sys.exit()

print('Yes') if '7' in strN else print('No')