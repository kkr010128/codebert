n = int(input())
arr = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
    s = input().split(" ")
    nums = list(map(int, s))
    arr[nums[0]-1][nums[1]-1][nums[2]-1] += nums[3]
for k in range(4):
    for j in range(3):
        for i in range(10):
            print(" {0}".format(arr[k][j][i]),end="")
        print("")
    if k < 3:
        for l in range(20):
            print("#",end="")
        print("")