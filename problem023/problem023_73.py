n = int(input())
h = {}

for i in range(n):
    op, st = input().split()
    if op == 'insert':
        h[st] = 'yes'
    else:
        print (h.get(st, 'no'))