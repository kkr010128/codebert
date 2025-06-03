s = range(1,14)
h = range(1,14)
c = range(1,14)
d = range(1,14)
n = int(raw_input())
for i in range(0,n):
    input_line = raw_input().split()
    mark = input_line[0]
    num = int(input_line[1])
    if mark == "S":
        s.remove(num)
    elif mark == "H":
        h.remove(num)
    elif mark == "C":
        c.remove(num)
    elif mark == "D":
        d.remove(num)
for i in s:
    print "S " + str(i)
for i in h:
    print "H " + str(i)
for i in c:
    print "C " + str(i)
for i in d:
    print "D " + str(i)