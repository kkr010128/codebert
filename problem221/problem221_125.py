import sys
S = input()

if not S.islower(): sys.exit()
if not ( 1 <= len(S) <= 100 ): sys.exit()

print('x'*len(S))