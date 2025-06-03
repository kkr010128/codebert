N=int(input())
S=[input()for _ in range(N)]
from collections import*
C=Counter(S)
print('AC','x',C['AC'])
print('WA','x',C['WA'])
print('TLE','x',C['TLE'])
print('RE','x',C['RE'])