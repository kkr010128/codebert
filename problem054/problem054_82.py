from itertools import *
c = [f'{x} {y}' for x, y in product('SHCD', range(1, 14))]
for _ in range(int(input())):
    c.remove(input())
if c: print(*c, sep='\n')
