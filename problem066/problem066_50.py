while True:
    s = list(input())
    if s[0] == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print("".join(s))

