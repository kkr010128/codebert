n = int(input())

added_strings = set()
for i in range(n):
    com, s = input().split()
    if com == 'insert':
        added_strings.add(s)
    elif com == 'find':
        print('yes' if (s in added_strings) else 'no')
