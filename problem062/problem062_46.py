while True:
    s = input()
    if len(s) == 1 and s[0] == '0': break
    total = 0
    for i in range(0,len(s)):
        total += int(s[i])
    print("%d" % total)