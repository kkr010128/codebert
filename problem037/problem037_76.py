S = int(input())
S = S % (24 * 3600)
hour = S // 3600
S %= 3600
minutes = S // 60
S %= 60
seconds = S
print("%d:%d:%d" % (hour, minutes, seconds))

