n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
nums = [[[0 for i in range(10)] for i in range(3)] for i in range(4)]
for d in data:
    nums[d[0] - 1][d[1] - 1][d[2] - 1] += d[3]
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(' ' + str(nums[i][j][k]), end='')
        print('')
    if i != 3:
        print('#' * 20)