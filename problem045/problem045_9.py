ls = map(float, raw_input().split())
d = (ls[0]/ls[1])
r = (ls[0]%ls[1])
f = ls[0]/ls[1]
print '%d %d %f' % (d, r, f)