#Good question
import sys
S = input()
if not S.islower(): sys.exit()
if not ( 1 <= len(S) <= 100 ):sys.exit()

pos = int(len(S)/2)

count = 0
for I in range(pos):
    if S[I] != S[-I-1]:
        count += 1
print(count)