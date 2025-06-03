t = input()

h = t / 3600
t %= 3600

m = t / 60
s = t % 60

print str(h) + ":" + str(m) + ":" + str(s)