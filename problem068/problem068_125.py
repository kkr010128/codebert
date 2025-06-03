s = input()
q = int(input())
for _ in range(q):
    x = input().split()
    a, b = int(x[1]), int(x[2])
    if x[0] == 'print':
        print(s[a:b+1])
    if x[0] == 'reverse':
        s = s[:a] + ''.join(reversed(s[a:b+1])) + s[b+1:]
    if x[0] == 'replace':
        s = s[:a] + x[3] + s[b+1:]