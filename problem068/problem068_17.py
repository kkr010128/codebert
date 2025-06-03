s = list(input())
q = int(input())
for i in range(q):
    cmd = list(input().split())
    m = int(cmd[1])
    n = int(cmd[2])
    if cmd[0] == "print":
        for i in range(m, n + 1):
            print(s[i], end="")
        print()

    if cmd[0] == "reverse":
        half = int((n - m) / 2)
        while m <= half\
        or    m < n:
            t = s[m]
            s[m] = s[n]
            s[n] = t
            m += 1 
            n -= 1
    if cmd[0] == "replace":
        r = cmd[3]
        j = 0
        for i in range(m, n + 1):
            s[i] = r[j]
            j += 1