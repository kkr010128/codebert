W, H, x, y, r = map(int, raw_input().split())
if x < r:
    print 'No'
elif W - x < r:
    print 'No'
elif y < r:
    print 'No'
elif H - y < r:
    print 'No'
else:
    print 'Yes'