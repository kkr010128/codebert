s = input()
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'replace':
        a,b = map(int,command[1:3])
        s = s[:a]+ command[3] + s[b+1:]
    elif command[0] == 'reverse':
        a,b = map(int,command[1:3])
        s = s[0:a] + s[a:b+1][::-1] + s[b+1:]
    elif command[0] == 'print':  
        a,b = map(int,command[1:3])
        print(s[a:b+1])
