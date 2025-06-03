while True:
    string = input().strip()
    if string == '0':   break
    print(sum([int(c) for c in string]))
