string = input()
n = int(input())
for _ in range(n):
    query = input().split()
    if query[0] == 'replace':
        op, a, b, p = query
        a, b = int(a), int(b)
        string = string[:a] + p + string[b + 1:]
    elif query[0] == 'reverse':
        op, a, b = query
        a, b = int(a), int(b)
        string = string[:a] + ''.join(reversed(string[a:b + 1])) + string[b + 1:]
    elif query[0] == 'print':
        op, a, b = query
        a, b = int(a), int(b)
        print(string[a: b + 1])