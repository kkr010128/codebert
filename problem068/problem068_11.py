s = input()
for _ in range(int(input())):
    o = input().split()
    a, b = map(int, o[1:3])
    b += 1
    c = o[0][2]
    if c == 'p':
        s = s[:a]+o[3]+s[b:]
    elif c == 'i':
        print(s[a:b])
    elif c == 'v':
        s = s[:a]+s[a:b][::-1]+s[b:]

