S = input()

s = list(S)
f = s[:int((len(s)-1)/2)]
l = s[int((len(s)+3)/2-1):]

if f == l:
    while len(f) > 1:
        if f[0] == f[-1]:
            f.pop(0)
            f.pop()
    if len(f) <= 1:
        while len(l) > 1:
            if l[0] == l[-1]:
                l.pop(0)
                l.pop()
        if len(l) <= 1:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')