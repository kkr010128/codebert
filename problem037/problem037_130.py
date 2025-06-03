S = int(raw_input())

h = S / 3600
m = S - 3600*h
s = m % 60
m = (m - s)/60

print str(h) + ":" + str(m) + ":" + str(s)