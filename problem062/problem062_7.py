while 1:
    x = input()
    if x == "0":
        break
    kei = 0
    for i in x:
        kei += int(i)
    print(kei)