str = list(input())
q = int(input())
for i in range(q):
    s = list(input().split())
    s[1] = int(s[1])
    s[2] = int(s[2])
    if s[0] == 'print':
        print(''.join(str[s[1]:s[2]+1]))
    elif s[0] == 'reverse':
        str[s[1]:s[2]+1] = ''.join(reversed(str[s[1]:s[2]+1]))
    elif s[0] == 'replace':
        str[s[1]:s[2]+1:1] = s[3]