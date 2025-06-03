while True:
    s = raw_input()
    if(s == "-"):
        break
    m = input()
    for i in range(m):
        h = input()
        temp = ""
        for j in range(h, len(s)):
            temp += s[j]
        for j in range(h):
            temp += s[j]
        s = temp
    print(s)