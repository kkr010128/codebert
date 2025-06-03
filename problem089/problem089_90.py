from sys import stdin
import collections

input = stdin.readline

Y, X, M = map(int, input().split())
bomb = set([tuple(map(int,inp.split())) for inp in stdin.read().splitlines()])
cx = collections.defaultdict(int)
cy = collections.defaultdict(int)
for y,x in bomb:
    cx[x] += 1
    cy[y] += 1
mx = max(cx.values())
my = max(cy.values())
candidateX = [x for (x,v) in cx.items() if v == mx]
candidateY = [y for (y,v) in cy.items() if v == my]
res = mx + my -1
for x in candidateX:
    for y in candidateY:
        if (y,x) not in bomb:
            res += 1
            break
    else:
        continue
    break
print(res)