s = input()
n = int(input())

for _ in range(n):
    line = input().split()
    order = line[0]
    a = int(line[1])
    b = int(line[2])
    p = line[3] if len(line) == 4 else ''

    if order == 'print':
        print(s[a:b+1])
    elif order == 'reverse':
        s = s[:a] + ''.join(reversed(s[a:b+1])) + s[b+1:]
    elif order == 'replace':
        s = s[:a] + p + s[b+1:]