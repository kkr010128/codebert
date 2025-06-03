# Next Alphabet
C = input()

from string import ascii_lowercase as alp
ans = alp[alp.index(C) + 1]
print(ans)
