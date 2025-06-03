def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    threshold = sum(A) / (4 * M)
    if sorted(A, reverse=True)[M-1] >= threshold:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
