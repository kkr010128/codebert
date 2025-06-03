import sys
K,X = map(int,input().split())
if not ( 1 <= K <= 100 and 1 <= X <= 10**5 ): sys.exit()

print('Yes') if 500 * K >= X else print('No')