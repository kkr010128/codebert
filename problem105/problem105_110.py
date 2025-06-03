def main():
    _ = int(input())
    num_tuple = tuple(map(int, input().split()))

    count = 0
    for i, num in enumerate(num_tuple):
        if ((i+1)*num) % 2 == 1:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
