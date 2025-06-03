while True:
    line = input()
    if line == '0':
        break

    n = 0
    for c in line:
        n += int(c)
    print(n)