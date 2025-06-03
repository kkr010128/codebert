def main():
    N, K = (int(x) for x in input().split())
    scores = [int(x) for x in input().split()]

    first, last = 0, K-1

    while last < N-1:
        last += 1
        if scores[first] < scores[last]: print('Yes')
        else: print('No')
        first += 1

if __name__ == '__main__':
    main()