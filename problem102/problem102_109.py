def main():
    n, k = [int(x) for x in input().split()]
    scores = [int(x) for x in input().split()]

    for index in range(n - k):
        if scores[index] < scores[index + k]:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
