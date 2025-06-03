import sys
S = input()
T = input()

if not ( 1 <= len(S) <= 2*10**5 ): sys.exit()
if not ( len(S) == len(T) ): sys.exit()
if not ( S.islower() and T.islower() ): sys.exit()

count = 0
for I in range(len(S)):
    if S[I] != T[I]:
        count += 1 
print(count)