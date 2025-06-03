d = list(map(int, input().split()))
op = list(input())

for o in op:
    b = [x for x in d]
    if o == "S":
        b[0] = d[4]
        b[1] = d[0]
        b[4] = d[5]
        b[5] = d[1]
    elif o == "E":
        b[0] = d[3]
        b[2] = d[0]
        b[3] = d[5]
        b[5] = d[2]
    elif o == "W":
        b[0] = d[2]
        b[2] = d[5]
        b[3] = d[0]
        b[5] = d[3]
    elif o == "N":
        b[0] = d[1]
        b[1] = d[5]
        b[4] = d[0]
        b[5] = d[4]
    for i in range(6):
        d[i] = b[i]

print(d[0])

