a = []
while True:
    b = map(int,raw_input().split())
    if b == [0, 0]:
        break
    a.append(b)
for list in a:
    h, w = list
    k = 0
    l = 0
    x = []
    y = []
    while k < w:
        if k % 2 == 0:
            x.append('#')
            y.append('.')
        else:
            x.append('.')
            y.append('#')
        k = k + 1
    while l < h:
        if l % 2 == 0:
            print ''.join(x)
        else:
            print ''.join(y)
        l += 1
    print 