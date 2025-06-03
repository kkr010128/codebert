def main():
    log_no, cut_max = [int(x) for x in input().split()]
    logs = [int(x) for x in input().split()]
    bin_l, bin_r = 0, 10 ** 9
    while bin_r - bin_l > 1:
        bin_mid = (bin_l + bin_r) // 2
        cut_count = sum((log - 1) // bin_mid for log in logs)
        if cut_count <= cut_max:
            bin_r = bin_mid
        else:
            bin_l = bin_mid
    print(bin_r)


if __name__ == '__main__':
    main()
