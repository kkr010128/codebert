time = int(input())

hour = int(time / 3600)
minute = int(time % 3600/60)
second = int(time % 60 % 60)

print("%d:%d:%d" % (hour, minute, second))

