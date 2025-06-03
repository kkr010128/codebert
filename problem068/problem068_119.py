text = list(input())
num = int(input())
for i in range(num):
    cmd = input().split()
    start, end = map(int, cmd[1:3])
    if cmd[0] == 'replace':
        text[start:end+1] = list(cmd[-1])
    elif cmd[0] == 'reverse':
        text[start:end+1] = (text[start:end+1])[::-1]
    elif cmd[0] == 'print':
        print(''.join(text[start:end+1]))
