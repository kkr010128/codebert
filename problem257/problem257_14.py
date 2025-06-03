def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    number = 1
    count = 0

    for i in range(n):
        if a_lst[i] == number:
            number += 1
        else:
            count += 1

    if 1 not in a_lst:
        count = -1

    print(count)


if __name__ == '__main__':
    main()