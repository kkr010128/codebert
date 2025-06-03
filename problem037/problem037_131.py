a = int(raw_input())
h = a / 3600
m = (a % 3600) / 60
s = a % 60
print "{0}:{1}:{2}".format(h, m, s)