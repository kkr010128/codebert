while True:
    a = input()
    b = a.split(' ')
    b.sort(key=int)
    if int(b[0]) == 0 and int(b[1]) == 0:
        break
    print('%s %s' % (b[0],b[1]))