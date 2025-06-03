while 1:
    s = input()
    if s[0] == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)