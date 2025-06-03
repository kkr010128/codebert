def aizu007():
    xs = map(int,raw_input().split())
    a,b,c = xs[0],xs[1],xs[2]
    cnt = 0
    for i in range(a,b+1):
        if c%i == 0:
            cnt = cnt + 1
    print cnt
aizu007()