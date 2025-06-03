n = int(input())
d = [list(map(int, input().split())) for _i in range(n)]

c = 0
for i, j in d:
    if i==j:
        c += 1
        if c == 3:
            print('Yes')
            import sys
            sys.exit()
    else:
        c = 0
print('No')