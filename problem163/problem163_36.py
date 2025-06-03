def main():
    sw = [int(_x) for _x in input().split()]
    s = sw[0]
    w = sw[1]
    if w >= s:
        print("unsafe")
    else:
        print("safe")


main()
