# coding=utf-8

inputs = raw_input().rstrip().split()
a, b, c = [int(x) for x in inputs]
if a < b < c:
    print 'Yes'
else:
    print 'No'