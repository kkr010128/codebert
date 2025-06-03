import sys
import collections

S=collections.deque(input())
Q=int(input())

rev=0
for _ in range(Q):
    fields=next(sys.stdin).split()
    T,F,C=(fields+['',''])[:3]
    if T=='1':
        rev^=1
    elif (rev and F=='1') or (not rev and F=='2'):
        S.append(C)
    else:
        S.appendleft(C)

if rev:
    print(''.join(reversed(S)))
else:
    print(''.join(S))
