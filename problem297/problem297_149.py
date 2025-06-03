import sys
N = int(input())

if not ( 1 <= N <= 100 ):sys.exit()

print(1-(int(N/2)/N))