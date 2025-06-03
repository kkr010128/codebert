while True:
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if a == 0 and b == 0:
        break
    elif a > b:
        print('{0} {1}'.format(b, a))
    else:
        print('{0} {1}'.format(a, b))