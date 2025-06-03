s = set()

for _ in range(int(input())):
    cmd, v = input().split()
    if cmd == 'insert':
        s.add(v)
    else:
        print('yes' if v in s else 'no')

