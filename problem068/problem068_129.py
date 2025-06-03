string = raw_input()
for _ in xrange(input()):
    order = raw_input().split()
    a, b = map(int, order[1:3])
    if order[0] == 'print':
        print string[a:b+1]
    elif order[0] == 'reverse':
        # string = string[:a] + string[b:a-1:-1] + string[b+1:]
        string = string[:a] + string[a:b+1][::-1] + string[b+1:]
    elif order[0] == 'replace':
        string = string[:a] + order[3] + string[b+1:]