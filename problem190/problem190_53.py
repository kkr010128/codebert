import sys
S = input()

if not S.islower():sys.exit()
if not ( 3 <= len(S) <= 99 and len(S) % 2 == 1 ): sys.exit()

# whole check
first = int((len(S)-1)/2)
F = S[0:first]
last = int((len(S)+3)/2)
L = S[last-1:]
condition = 0
if S == S[::-1]:
    condition += 1
if F == F[::-1]:
    condition += 1
if L == L[::-1]:
    condition += 1

print('Yes') if condition == 3 else print('No')