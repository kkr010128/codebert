sec = int(input())
m, s = divmod(sec, 60)
h, m = divmod(m, 60)

print('%d:%d:%d' % (h, m, s))