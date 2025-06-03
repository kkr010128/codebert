#coding: utf-8
def GCM(m, n):
    while 1:
        if n == 0: return m
        m -= (m/n)*n
        m,n = n,m
    
while 1:
    try:
        a,b = map(int, raw_input().split())
        x = GCM(a,b)
        y = a*b / x
        print "%d %d" % (x, y)
    except EOFError:
        break