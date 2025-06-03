s = input()

for i in range(int(input())):
    cmd = input().split()
    a, b = int(cmd[1]), int(cmd[2])

    if cmd[0] == 'print':
        print(s[a:b+1])
    elif cmd[0] == 'reverse':
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif cmd[0] == 'replace':
        s = s[:a] + cmd[3] + s[b+1:]