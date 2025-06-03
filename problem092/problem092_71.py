x,k,d = map(int,input().split())

def judge():
    l = x if x > 0 else -x
    i = l//d
    r = l%d

    if (k - i)%2 == 0:
        print(r)
    else:
        print(d - r)
    '''
    if x > 0:
        for r in range(d):
            if (x - r)/d == (x - r)//d:
                i = (x - r)//d
                if (k - i)%2 == 0:
                    print(r)
                else:
                    print(d-r)
                exit()
    else:
        l = -x
        for r in range(d):
            if (l - r)/d == (l - r)//d:
                i = (l - r)//d
                if (k - i)%2 == 0:
                    print(r)
                else:
                    print(d-r)
                exit()
    '''

if x == 0:
    if k%2 == 0:
        print(0)
    else:
        print(d)
elif x < 0:
    if k*d + x > 0:
        judge()
    else:
        print(abs(k*d + x))
else:
    if x - k*d < 0:
        judge()
    else:
        print(abs(x - k*d))
