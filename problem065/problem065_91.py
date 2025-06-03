W = raw_input().lower()
c = 0

while True:
    T = raw_input()
    if T == "END_OF_TEXT":
        break
    Ti = T.lower().split()
    for i in Ti:
        if i == W:
            c += 1

print("%d" % (c, ))