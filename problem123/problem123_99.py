def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    all_xor = 0
    for a in a_list:
        all_xor ^= a

    x_list = [a ^ all_xor for a in a_list]

    print(*x_list, sep=" ")


if __name__ == "__main__":
    main()
