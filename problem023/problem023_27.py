s = set()
for _ in range(int(input())):
    c = input().split()
    if c[0] == 'insert':
        s.add(c[1])
    else:
        print('yes' if c[1] in s else 'no')