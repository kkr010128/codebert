t1, t2 = [ int(v) for v in input().split() ]
a1, a2 = [ int(v) for v in input().split() ]
b1, b2 = [ int(v) for v in input().split() ]

if a1*t1 + a2*t2 == b1*t1 + b2*t2:
    ans = -1
else:
    if a1*t1 + a2*t2 < b1*t1 + b2*t2:
        a1, b1 = b1, a1
        a2, b2 = b2, a2

    mind = a1*t1 - b1*t1
    if mind > 0:
        ans = 0
    else:
        lastd = a1*t1 + a2*t2 - b1*t1 - b2*t2
        mind = abs(mind)
        if mind % lastd == 0:
            ans = 2 * (mind // lastd) 
        else:
            ans = 2 * (mind // lastd) + 1
    
print(ans if ans != -1 else "infinity")