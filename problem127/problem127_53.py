x, y = map(int, input().split())
for a in range(0, 101):
    for b in range(0, 101):
        if a + b == x and 2*a + 4*b == y:
            print('Yes')
            exit()
print('No')