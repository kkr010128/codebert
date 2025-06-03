import sys
N = int(input())
S,T = input().split()

if not ( 1 <= N <= 100 ): sys.exit()
if not ( len(S) == len(T) and len(S) == N ): sys.exit()
if not ( S.islower() and T.islower() ): sys.exit()

for I in range(N):
    print(S[I],end='')
    print(T[I],end='')