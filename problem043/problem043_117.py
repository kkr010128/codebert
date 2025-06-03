tmp = 0
while True:
    i = raw_input().strip().split()
    a = int(i[0])
    b = int(i[1])
    if a == 0 and b == 0:
        break
    if a > b:
        tmp = a
        a = b
        b = tmp
    print a,b