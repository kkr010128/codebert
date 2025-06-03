str = list(input())
for _ in range(int(input())):
    cmd = input().split()
    a, b = map(int, cmd[1:3])
    if cmd[0] == 'print':
        for i in range(a, b + 1):
            print(str[i], end='')
        print('')
    if cmd[0] == 'reverse':
        str = str[:a] + list(reversed(str[a:b + 1])) + str[b + 1:]
    if cmd[0] == 'replace':
        p = cmd[3]
        str = str[:a] + list(p) + str[b + 1:]