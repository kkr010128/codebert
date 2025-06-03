data = []
while True:
    in_line = raw_input().split()
    m = int(in_line[0])
    f = int(in_line[1])
    r = int(in_line[2])
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        data.append("F")
    elif m + f >= 80:
        data.append("A")
    elif m + f >= 65:
        data.append("B")
    elif m + f >= 50:
        data.append("C")
    elif m + f >= 30:
        if r >= 50:
            data.append("C")
        else:
            data.append("D")
    else:
        data.append("F")
for n in data:
    print n