import sys
S,T = input().split()

if not ( S.islower() and T.islower() ): sys.exit()
if not ( 1 <= len(S) <= 100 and 1 <= len(S) <= 100 ): sys.exit()

print(T,S,sep='')