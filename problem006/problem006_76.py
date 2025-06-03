n = input()
s = 100000
for i in range(n):
    s = s * 1.05
    if s % 1000 != 0:
        s = ((s // 1000) + 1) * 1000
print "%d" % s