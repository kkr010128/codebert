a = []
while True:
    b = map(int, raw_input().split())
    if b == [0, 0]:
        break
    a.append(b)
for list in a:
    h, w = list
    k = 0
    l = 0
    x = []
    while k < w:
        x.append('#')
        k = k + 1
    while l < h:
        print ''.join(x)
        l = l + 1
    print 