n = int(input())
d = set()
for _ in range(n):
    c, s = input().split()
    if c == 'insert':
        d.add(s)
    else:
        print('yes' if s in d else 'no')
