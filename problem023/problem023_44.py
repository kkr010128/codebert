n = int(input())
D = set()
for _ in range(n):
    q, s = map(str, input().split())
    if q == 'insert':
        D.add(s)
    elif q == 'find':
        if s in D:
            print('yes')
        else:
            print('no')
