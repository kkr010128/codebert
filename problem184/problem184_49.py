import sys

S = input()
if not ( len(S) == 6 and S.islower() ): sys.exit()
print('Yes') if S[2] == S[3] and S[4] == S[5] else print('No')