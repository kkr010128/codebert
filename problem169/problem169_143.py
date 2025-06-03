def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    lst = [0 for _ in range(2 * 10 ** 5 + 1)]

    for a in a_lst:
        lst[a] += 1

    for i in range(1, n + 1):
        print(lst[i])


if __name__ == "__main__":
    main()
