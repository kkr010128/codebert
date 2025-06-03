n = int(input())
d = [list(map(int, input().split())) for i in range(n)]
def zoro(items):
    return items[0] == items[1]
for a, b, c in zip(d[:], d[1:], d[2:]):
    if zoro(a) and zoro(b) and zoro(c):
        print('Yes')
        exit(0)
print('No')
    
