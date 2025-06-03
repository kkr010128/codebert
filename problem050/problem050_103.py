while True:
    H, W = map(int, raw_input().split())
    if (H+W) == 0:
        break
    print_dot = "#" + ('.'*(W-2)) + "#"
    print "#"*W
    for h in range(1, (H-1)):
        print print_dot
    print "#"*W
    print ""