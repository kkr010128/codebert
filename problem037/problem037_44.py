t = int(input(''))

s = t % 60
h = t // (60 * 60)
m = (t % 3600) // 60

print(str(h) + ":" + str(m) + ":" + str(s))
