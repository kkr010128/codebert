if __name__ == '__main__':
    W, H, x, y, r = map(int, raw_input().split())

    ret = "Yes"
    if W < x + r or x - r < 0 or H < y + r or y - r < 0:
        ret = "No"

    print ret