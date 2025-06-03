import sys
N,K = map(int,input().split())
array = [ I for I in map(int,input().split()) if (1 <= I <= 1000) ]

if not ( 1 <= K <= N and K <= N <= 1000 ): sys.exit()

print(sum(sorted(array)[:K]))