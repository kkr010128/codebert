import sys

sec_1 = sys.stdin.readline()

sec_1 = int(sec_1)

hour = sec_1 / 3600

min = sec_1 / 60 - hour * 60

sec = sec_1 % 60

print '%d:%d:%d' % (hour, min, sec)