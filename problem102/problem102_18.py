def main():
    n, k = [int(x) for x in input().split()]
    scores = [int(x) for x in input().split()]

    for old, new in zip(scores, scores[k:]):
        if old < new:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
