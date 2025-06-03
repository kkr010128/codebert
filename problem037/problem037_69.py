time = raw_input()
time = int(time)
h = time / 3600
m = (time - h * 3600) / 60
s = time - (h * 3600 + m * 60)
print "%d:%d:%d" % (h, m, s)