def main():
    n = int(input())

    s_dict = dict()
    for _ in range(n):
        s = input()
        if s in s_dict:
            continue
        else:
            s_dict[s] = 1

    print(sum(s_dict.values()))


if __name__ == "__main__":
    main()
