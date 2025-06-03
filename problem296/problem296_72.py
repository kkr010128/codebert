S = input()
k = int(input())
from itertools import groupby
x = y = 0
g = [len(list(v)) for k,v in groupby(S)]
for c in g:
    x += c//2
#print(len(S),g[0])
if S[-1] == S[0]:
    if g[-1]%2 == 0 or g[0]%2 == 0:
        pass
    elif len(S) == 1:
        y = k//2
    elif len(S) == g[0]:
        y = k//2
        #print('?',y)
    else:
        y = k-1
print(x*k + y)
