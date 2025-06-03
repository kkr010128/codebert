if __name__ == '__main__':
    k = int(input())
    s = list(input())

    if len(s) <= k:
        print(''.join(s))
    else:
        print(''.join(s[:k]) + '...')