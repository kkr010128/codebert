number = raw_input().split(" ")
a, b, c = int(number[0]), int(number[1]), int(number[2])
while True:
    if a > b:
        tmp = a
        a = b
        b = tmp
    elif b > c:
        tmp = b
        b = c
        c = tmp
    else:
        print str(a) + " " + str(b) + " " + str(c)
        break