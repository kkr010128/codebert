while True:
    s = input()
    if s == "-":
        exit()
    m = int(input())
    for i in range(m):
        h = int(input())
        s = s[h:] + s[:h]
    print(s)
