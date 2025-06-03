while True:
    a = raw_input()
    if a == '-':
        break
    m = input()
    b = [input() for _ in range(m)]
    for i in b:
        a =  a[i:]+a[0:i]
    print a