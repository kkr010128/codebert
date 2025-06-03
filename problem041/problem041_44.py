# coding=utf-8

inputs = raw_input().rstrip().split()
W, H, x, y, r = [int(x) for x in inputs]

if 0 <= x - r and x + r <= W and 0 <= y - r and y + r <= H:
    print 'Yes'
else:
    print 'No'