if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    threshold = total / (4*M)
    count = sum([a>=threshold for a in A])
    if count >= M:
        print('Yes')
    else:
        print('No')

