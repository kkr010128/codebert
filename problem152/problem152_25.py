from operator import itemgetter
from itertools import chain


N = int(input())
L = []
R = []
for i in range(N):
    S = input()
    low = 0
    var = 0

    for s in S:
        if s == '(':
            var += 1
        else:
            var -= 1
        low = min(low, var)
    
    if var >= 0:
        L.append((low, var))
    else:
        R.append((low, var))

L.sort(key=itemgetter(0), reverse=True)
R.sort(key=lambda x: x[0] - x[1])
pos = 0
for i, (low, var) in enumerate(chain(L, R)):
    if pos + low < 0:
        ans = 'No'
        break
    pos += var
else:
    ans = 'Yes' if pos == 0 else 'No'
print(ans)
