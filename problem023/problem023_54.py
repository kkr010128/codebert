n = int(input())
d = {}

for i in range(n):
    order = input().split()
    if order[0] == 'insert':
        d[order[1]] = i
    else:
        if order[1] in d:
            print("yes")
        else:
            print("no")