Str = input()
q = int(input())
for i in range(q):
    order = list(input().split())
    o = order[0]
    a = int(order[1])
    b = int(order[2])
    
    if o=='print':
        print(Str[a:b+1])
    
    if o=='reverse':
        StrL = list(Str)
        t = list(Str[a:b+1])
        j = len(t)-1
        for i in range(a,b+1):
            StrL[i] = t[j]
            j -= 1
        Str = ''.join(StrL)
    
    if o=='replace':
        p = list(order[3])
        StrL = list(Str)
        j = 0
        for i in range(a,b+1):
            StrL[i] = p[j]
            j += 1
        Str = ''.join(StrL)
