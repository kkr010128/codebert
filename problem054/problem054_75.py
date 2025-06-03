from itertools import*
c=[f'{x} {y}'for x,y in product('SHCD',range(1,14))]
exec('c.remove(input());'*int(input()))
if c:print(*c,sep='\n')
