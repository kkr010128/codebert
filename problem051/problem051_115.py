while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    t = "{0}{1}" * (b//2) + ("\n" if b % 2 == 0 else "{0}\n")
    t1 = t.format("#",".")
    t2 = t.format(".","#")
    print((t1+t2) * (a//2) + ("" if a % 2 == 0 else t1))