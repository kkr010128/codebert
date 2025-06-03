string = input()
for _ in range(int(input())):
    com = [x for x in input().split()]
    c = com[0]
    a,b = [int(com[i]) for i in range(1,3)]
    if c == 'reverse':
        string = string[:a] + string[a:b+1][::-1] + string[b+1:]
    if c == 'print':
        print(string[a:b+1])
    if c == 'replace':
        string = string[:a] + com[3] + string[b+1:]

