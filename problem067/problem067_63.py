n = int(input())
x, y = 0, 0
for _ in range(n):
    info = input().split()
    if info[0] > info[1]:
        x += 3
    elif info[0] < info[1]:
        y += 3
    else:
        x += 1
        y += 1
print(x, y)
