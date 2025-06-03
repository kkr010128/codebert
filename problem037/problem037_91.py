S = raw_input()
S = int(S)
h = S / 3600
m = (S - h * 3600) / 60
s = S - 3600 * h - 60 * m

print u"%d:%d:%d" % (h,m,s)