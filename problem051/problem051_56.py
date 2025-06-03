def gen(n):
    g = '#.'
    while True:
        yield g[n%2]
        n += 1

while True:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    for i in xrange(H):
        g = gen(i)
        print ''.join([g.next() for j in xrange(W)])
    print 