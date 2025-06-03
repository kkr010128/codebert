while True:
    s = raw_input()
    if s == "-":
        break
    m = int(raw_input())
    for i in range(m):
        n = int(raw_input())
        s = s[n:]+s[:n]
    print s
