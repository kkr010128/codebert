str = input()
n = int(input())

for i in range(n):
    args = input().split()
    command = args[0]
    s = int(args[1])
    e = int(args[2])
    if command == 'print':
        print(str[s:e + 1])
    if command == 'reverse':
        str = str[0:s] + str[s:e + 1][::-1] + str[e + 1:]
    if command == 'replace':
        str = str[0:s] + args[3] + str[e + 1:]