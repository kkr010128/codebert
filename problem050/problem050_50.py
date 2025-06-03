while True:
    a, b = map(int, raw_input().split(' '))
    if a == 0 and b == 0:
        break
    for i in range(a):
        if b == 1:
            print "#"
        elif i == 0:
            print "#" * b
        elif i == a - 1:
            print "#" * b
        else:
            print "#" + "." * (b-2) + "#"
    print ''