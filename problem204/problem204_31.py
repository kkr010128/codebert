S = input()
Q= int(input())
r = False
h = []
t = []
for i in range(Q):
    Query = input().split()
    if int(Query[0]) == 1:
        r = not r
    else:
        if int(Query[1]) == 1 and not r or int(Query[1]) == 2 and r:
            h.append(Query[2])
        else:
            t.append(Query[2])
if not r:
    print(''.join(reversed(h))+S+''.join(t))
else:
    print(''.join(reversed(t))+S[::-1]+''.join(h))
