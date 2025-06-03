house1 = [[0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)]]
house2 = [[0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)]]
house3 = [[0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)]]
house4 = [[0 for x in range(10)], [0 for x in range(10)], [0 for x in range(10)]]
houses = [house1, house2, house3, house4]

n = int(input())

for i in range(n):
    b, f, r, v = [int(x) for x in input().split()]
    houses[b - 1][f - 1][r - 1] += v

cnt = 0
for house in houses:
    for floor in house:
        floor = [str(x) for x in floor]
        print(' ' + ' '.join(floor))
    if cnt != 3:
        print('#' * 20)
    cnt += 1