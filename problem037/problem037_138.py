a = input()

s = a % 60
a = (a - s) / 60
m = a % 60
a = (a - m) / 60
h = a

print "%s:%s:%s" % (str(h), str(m), str(s))