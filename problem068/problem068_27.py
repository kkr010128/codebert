s = input()
q = int(input())
for i in range(q):
    command = input().split()
    command[1] = int(command[1])
    command[2] = int(command[2])
    if command[0] == 'print':
        print(s[command[1]:command[2]+1])
    elif command[0] == 'reverse':
        s = s[command[1]:command[2]+1][::-1].join([s[:command[1]], s[command[2]+1:]])
    elif command[0] == 'replace':
        s = command[3].join([s[:command[1]], s[command[2]+1:]])