x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p.sort()
q.sort()
r.sort(reverse=True)

ppick = p[-x:]
qpick = q[-y:]
pi = 0
qi = 0

for i in range(len(r)):
    if pi >= x:
        while True:
            if qi < y and i < c and r[i] > qpick[qi]:
                qpick[qi] = r[i]
                qi += 1
                i += 1
            else:
                break
    elif qi >= y:
        while True:
            if pi < x and i < c and r[i] > ppick[pi]:
                ppick[pi] = r[i]
                pi += 1
                i += 1
            else:
                break
    elif ppick[pi] >= qpick[qi] and qpick[qi] < r[i]:
        qpick[qi] = r[i]
        qi += 1
        continue
    elif ppick[pi] < qpick[qi] and ppick[pi] < r[i]:
        ppick[pi] = r[i]
        pi += 1
        continue
    break

print(sum(ppick) + sum(qpick))
