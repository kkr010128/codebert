while True:
    s = raw_input()
    if '-' == s:
        break
    m = input()
    for a in range(m):
        h = input()
        s = s[h:len(s)]+s[:h]
    print s