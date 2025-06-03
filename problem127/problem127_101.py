x, y = map(int, input().split())

if y > x * 4:
    print("No")
else:
    for i in range(x + 1):
        if 2 * i + 4 * (x - i) == y:
            str = 'Yes'
            break
        else:
            str = 'No'

    print(str)
