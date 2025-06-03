while True:
    xy_list = list(map(int, input().split()))
    if xy_list[0] == xy_list[1] == 0:
        break
    print(*sorted(xy_list))