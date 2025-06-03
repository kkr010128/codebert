n = input()
d = 100000
for x in range(n):
        d += int(d*0.05)
        d = str(d)
        if d[-3:] != "000":
                d = d[:-3] + "000"
                d = int(d) +1000
        else:
                d = int(d)
print d