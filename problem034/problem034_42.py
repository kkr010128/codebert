axis_1 = '0154' * 2  # 2 -> 3
axis_2 = '0253' * 2  # 4 -> 1
axis_3 = '3124' * 2  # 0 -> 5

right = [axis_3, axis_2[::-1], axis_1, axis_1[::-1], axis_2, axis_3[::-1], ]
a = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    top, front = map(a.index, map(int, input().split()))
    x = '%d%d' % (top, front)
    for i, axis in enumerate(right):
        if x in axis:
            print(a[i])
            break
    else:
        print('------------------')
        print(x)