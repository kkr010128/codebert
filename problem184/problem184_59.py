import sys

S = input()
cond = (S[2]==S[3]) & (S[4]==S[5])

ans = "Yes" if cond else "No"
print(ans)