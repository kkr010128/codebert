S = int(raw_input())
M, s = S / 60, S % 60
h, m = M / 60, M % 60
print '%d:%d:%d' % (h, m, s)