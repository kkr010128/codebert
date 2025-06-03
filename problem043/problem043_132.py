while True:
    ins = input().split()
    x = int(ins[0])
    y = int(ins[1])
    if x == 0 and y == 0:
        break
    else:
        nums = [x, y]
        nums.sort()
        print(" ".join(map(str, nums)))